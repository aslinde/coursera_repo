from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime
def home(request):
    return HttpResponse("Welcome to the Littme Lemon restaurant")

def display_date(request):
    date_joihed = datetime.today().year
    return HttpResponse(date_joihed)
