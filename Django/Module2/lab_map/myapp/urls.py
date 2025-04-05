from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('menu/<int:number>', views.menu),
    re_path(r'book/[0-9]{1}/$', views.book),
]