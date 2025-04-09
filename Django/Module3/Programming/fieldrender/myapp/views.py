from django.shortcuts import render

# Create your views here.
from .forms import ApplicationForm 

def index(request): 
    form = ApplicationForm() ## Create Instance of the form
    context = {'form':form} # Dictionar
    return render(request, 'form.html', context) 
