from django.urls import path
from . import views

urlpatterns = [
    path('url/', views.home, name="home"),
    path('home/', views.home2, name="home2"),
]