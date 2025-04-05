from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    object = "<h1> Welcome to Little Lemon! </h1>"
    return HttpResponse(object)
def home2(request):
    path = request.path
    return HttpResponse(path, content_type='text/html', charset='utf-8')