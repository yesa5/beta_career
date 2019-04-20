from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from . import views

app_name = "vacancies"

urlpatterns = [
    path('', views.vacancy_list, name='vacancy_list'),
    path('<int:pk>/', views.vacancy_detail, name='vacancy_detail'),
]
