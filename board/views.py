from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from board.models import Ddate, Ddiary
from django.db import models
from calendar import HTMLCalendar
from django.utils.html import conditional_escape as esc
from django.views.generic import TemplateView
from django.utils.safestring import mark_safe

class MyCalendar(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        calendar_1 = HTMLCalendar(6).formatmonth(2017,6)
        return HttpResponse(mark_safe(calendar_1))
    

def index(request):
    diary_list = Ddate.objects.all().order_by('-pub_date')[:5]
    calendar_1 = HTMLCalendar(6).formatmonth(2017,6)
    calendar = conditional_escape(calendar_1)
    context = {'diary_list': diary_list, 'calendar': calendar_1}
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

