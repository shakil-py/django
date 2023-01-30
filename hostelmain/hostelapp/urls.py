from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static


app_name = "hostelapp"
urlpatterns = [
    path('', views.hostelapp),
    path('submit-form', views.aftersubmit),
    path("submit-form/", views.mealview),
    
]
