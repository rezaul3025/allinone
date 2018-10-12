from . import views
from django.urls import path

urlpatterns = [
    path('', views.DateTimeViews.index, name='index'),
    path('period_between_dates/', views.DateTimeViews.get_period_between_date_inputs, name='period_between_dates'),
]