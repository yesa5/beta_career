from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from . import views

app_name = "companies"

urlpatterns = [
    path('', views.company_list, name='company_list'),
    path('<int:pk>/', views.company_detail, name='company_detail'),
]
