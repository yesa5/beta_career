from django.urls import path
from . import views
app_name = "resumes"
urlpatterns = [
    path('<int:pk>', views.resume_detail, name='resume'),
]
