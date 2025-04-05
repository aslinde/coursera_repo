from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
def index(request): 
    return HttpResponse("Hello, world. This is the index view of Demoapp.")

def home(request):
    return HttpResponse("Hello, world. This is the home view of Demoapp.")