from django import forms    
from .models import logger

class logform(forms.ModelForm):
    class Meta:
        model = logger ## Model to be bound with form
        fields = '__all__'