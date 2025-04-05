from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Little Lemon restaurant")
def about(request):
    return HttpResponse("About us")
def menu(request, number):
    return HttpResponse("Menu, also your lucky number is {}".format(number))
def book(request):
    return HttpResponse("Make a booking")
