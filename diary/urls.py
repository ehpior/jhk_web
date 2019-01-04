from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:diary_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('create/make/', views.make, name='make'),
]