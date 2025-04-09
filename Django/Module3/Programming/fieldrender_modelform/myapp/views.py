from django.shortcuts import render

# Create your views here.
from .forms import logform

def index(request): 
    form = logform() ## Create Instance of the form
    if request.method == 'POST':
        form = logform(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form} # context Dictionary 
    return render(request, 'form.html', context) 
