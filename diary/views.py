from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from diary.models import Ddate, Ddiary
from django.db import models
import datetime
from calendar import HTMLCalendar
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

def index(request):
    diary_list = Ddate.objects.all()
#    diary_list = Ddate.objects.filter(id=11)
    calendar_1 = HTMLCalendar(6).formatmonth(2017,6)
    calendar = conditional_escape(calendar_1)
    context = {'diary_list': diary_list, 'calendar': mark_safe(calendar_1)}
    return render(request, 'diary/index.html', context)


def detail(request, diary_id):
    diary_content = get_object_or_404(Ddate, pk=diary_id)
    return render(request, 'diary/detail.html', {'diary_content': diary_content})


def create(request):
    return render(request, 'diary/create.html')


def make(request):
    if request.method == 'POST':
        new_Ddate = Ddate.objects.create(pub_date=request.POST['datetime'])
        new_Ddiary = Ddiary.objects.create(ddate=new_Ddate, dtitle=request.POST['title'], dcontent=request.POST['content'])
    return HttpResponseRedirect(reverse('diary:index'))

