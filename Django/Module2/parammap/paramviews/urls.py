from . import views
from django.urls import path

urlpatterns = [
    path('dishes/<str:drink>', views.drink_view, name="idkwhatthisdoes")
]
