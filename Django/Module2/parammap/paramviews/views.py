from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def drink_view(request, drink):
    items = {
        'pasta':'some wheat and a bit of italian love',
        'pizza':'saucy goodness',
        'ice cream':'delicious, creamy, natural'
    }
    description = items[drink]
    return HttpResponse('<h1>This is {}.<br> because it is {}</h1>'.format(description, drink))