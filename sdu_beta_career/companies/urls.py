from django.urls import path, include
from . import views

app_name = "companies"

urlpatterns = [
    path('', views.company_list, name='company_list'),
]
