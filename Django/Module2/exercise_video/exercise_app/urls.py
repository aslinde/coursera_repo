### This is the App level Urks file
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('date/', views.display_date)
]