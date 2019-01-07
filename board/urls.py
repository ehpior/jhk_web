from django.urls import path
from django.conf.urls import url
from .views import *

app_name = 'board'

urlpatterns = [
    path('', MyCalendar.as_view(), name='index'),
    #path('<int:question_id>/', views.detail, name='detail'),
    #path('<int:question_id>/results/', views.results, name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]