from django.urls import path
from .import views

app_name="hstelapp"
urlpatterns=[
    path("home/",views.hostelapp)
]