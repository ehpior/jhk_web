from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from diary.models import Ddate, Ddiary
from django.db import models
import datetime
from datetime import date
from calendar import HTMLCalendar
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

class mycalendar(HTMLCalendar):
    #cssclasses = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    cssclasses = ["a2", "a2", "a2", "a2", "a2", "a2", "a2"]
    cssclass_noday = "text-aasd"
    cssclasses_weekday_head = ["a1", "a1", "a1", "a1", "a1", "a1", "a1"]
    #cssclass_month = "text-bold text-red"
    #cssclass_month_head = "text-bold text-blue"
    def formatday(self, day, weekday):
        diary_list = Ddate.objects.all().order_by('-pub_date')
        if day > 0:
            cssclass = self.cssclasses[weekday]
            kkk = '-'.join(['2019-01',str(day).zfill(2)])
            kkk2 = Ddate.objects.filter(pub_date__icontains=kkk)
            body = ['<ul style="margin:-15px 0px; padding:0px 30px;">']
            body.append('<li style="margin-bottom:-25px"><h5>')
            if kkk2:
                body.append('<a href="/diary/')
                body.append(str(kkk2[0].id))
                body.append('">')
                body.append(str(kkk2[0].ddiary_set.first()))
                body.append('</a>')
            else:
                body.append('음슴')
            body.append('</h5></li><li><h5>')
            body.append('<a href="/diary/create">Create</a>')
            body.append('</h5></li></ul>')
            return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
        return self.day_cell('noday', day)

    def day_cell(cls, cssclasses, body):
        if body == 0:
            body = ''
        return '<td class="%s">%s</td>' % (cssclasses, body)
    

def index(request):
    diary_list = Ddate.objects.all().order_by('-pub_date')
    k1 = '2019'
    k2 = '1'
    k3 = '1'
    k4 = '-'.join([k1.zfill(4),k2.zfill(2),k3.zfill(2)])
    diary2 = Ddate.objects.filter(pub_date__icontains=k4)
    calendar_1 = mycalendar(6).formatmonth(2019,1)
    #calendar_1 = HTMLCalendar(6).formatmonth(2017,6)
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

