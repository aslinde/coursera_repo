from django.urls import path
from . import views
urlpatterns = [
    path('about/', views.About),
    path('menu/', views.Menu),
]