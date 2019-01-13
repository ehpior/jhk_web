from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from diary.models import Ddate, Ddiary
from django.db import models
import datetime
from datetime import date
from calendar import HTMLCalendar, month_name
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

class mycalendar(HTMLCalendar):
    #cssclasses = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    cssclasses = ["a2", "a2", "a2", "a2", "a2", "a2", "sun"]
    cssclass_noday = "text-aasd"
    cssclasses_weekday_head = ["a1", "a1", "a1", "a1", "a1", "a1", "sun1"]
    #cssclass_month = "text-bold text-red"
    cssclass_month_head = "month_1"
    def formatday(self, day, weekday):
        diary_list = Ddate.objects.all().order_by('-pub_date')
        if day > 0:
            cssclass = self.cssclasses[weekday]
            kkk = '-'.join([str(self.year),str(self.month).zfill(2),str(day).zfill(2)])
            kkk2 = Ddate.objects.filter(pub_date__icontains=kkk)
            body = ['<ul style="margin:-15px 0px; padding:0px 30px;">']
            body.append('<li style="margin-bottom:-10px"><h5>')
            if kkk2:
                body.append('<a href="/diary/')
                body.append(str(kkk2[0].id))
                body.append('">')
                body.append(str(kkk2[0].ddiary_set.first()))
                body.append('</a>')
            else:
                body.append('미작성')
            body.append('</h5></li><li><h5>')
            body.append('<a href="/diary/create">새로만들기</a>')
            body.append('</h5></li></ul>')
            return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
        return self.day_cell('noday', day)

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(mycalendar, self).formatmonth(year, month)

    def formatmonthname(self, year, month, withyear=True):
        if withyear:
            s = '%s %s' % (month_name[month], year)
        else:
            s = '%s' % month_name[month]
        return '<tr><th colspan="1" class="month_1">' \
               '<a href="%s">이전 달</a></th>' \
               '<th colspan="5" class="month_1">%s</th>' \
               '<th colspan="1" class="month_1">' \
               '<a href="%s">다음 달</th></tr>' \
               % (reverse('diary:index', kwargs=self.get_previous_month(year, month)), s,
                  reverse('diary:index', kwargs=self.get_next_month(year, month)))
    @classmethod
    def get_previous_month(cls, year, month):
        if month == 1:
            return {"year": year-1, "month": 12}
        else:
            return {"year": year, "month": month-1}

    @classmethod
    def get_next_month(cls, year, month):
        if month == 12:
            return {"year": year + 1, "month": 1}
        else:
            return {"year": year, "month": month + 1}

    def day_cell(cls, cssclasses, body):
        if body == 0:
            body = ''
        return '<td class="%s">%s</td>' % (cssclasses, body)
    

def index(request, **kwargs):
    diary_list = Ddate.objects.all().order_by('-pub_date')
    k1 = '2019'
    k2 = '1'
    k3 = '1'
    k4 = '-'.join([k1.zfill(4),k2.zfill(2),k3.zfill(2)])
    diary2 = Ddate.objects.filter(pub_date__icontains=k4)
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    if 'year' in kwargs and 'month' in kwargs:
        year = int(kwargs['year'])
        month = int(kwargs['month'])
    #calendar_1 = mycalendar(6).formatmonth(2019,1)
    calendar_1 = mycalendar(6).formatmonth(year,month)
    calendar = conditional_escape(calendar_1)
    context = {'diary_list': diary_list, 'diary2': diary2, 'calendar': mark_safe(calendar_1)}
    #context = {'diary_list': diary_list, 'calendar': mark_safe(calendar_1)}
    return render(request, 'diary/index.html', context)


def detail(request, diary_id):
    diary_content = get_object_or_404(Ddate, pk=diary_id)
    return render(request, 'diary/detail.html', {'diary_content': diary_content})


def create(request):
    return render(request, 'diary/create.html')


def make(request):
    if request.method == 'POST':
        new_Ddate = Ddate.objects.create(pub_date=request.POST['date'])
        new_Ddiary = Ddiary.objects.create(ddate=new_Ddate, dtitle=request.POST['title'], dcontent=request.POST['content'])
    return HttpResponseRedirect(reverse('diary:index'))

