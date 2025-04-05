from django import forms

class DemoForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea(attrs={'rows':5}), max_length=100)

class DemoForm2(forms.Form):
    name = forms.EmailField(widget=forms.Textarea(attrs={'rows':5}), max_length=100)
