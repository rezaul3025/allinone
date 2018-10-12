from . import views
from django.urls import path

urlpatterns = [
    path('', views.DoctorViews.index, name='index'),
]