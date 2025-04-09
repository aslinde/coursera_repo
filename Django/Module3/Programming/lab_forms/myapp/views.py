from django.shortcuts import render
from .forms import BookingForm
# Create your views here.
def index(request):
    form = BookingForm() ## Instantiate
    if request.method == 'POST':
        form = BookingForm(request.POST) ## Update the Object
        if form.is_valid(): ## Checks if Form valid and then saves if so
            form.save()
    context = {'form':form} ## returns renderable object as k-v pair
    return render(request, 'form.html', context) ## return the request using the template HTML using what the form is to process???