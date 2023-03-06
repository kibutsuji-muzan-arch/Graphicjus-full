from django import forms
from .models import Services, Contact
# from pyisemail import validate_email

class ContactForm(forms.ModelForm):

    email = forms.EmailField(max_length=60, required=True, widget=forms.EmailInput(attrs={'id':"email"}))
    name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'id':"name"}))
    services = forms.CharField(max_length=20, required=False)

    class Meta:
        model = Contact
        fields = ("email", "name","services")