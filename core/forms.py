from django import forms
from core.models import ContactUs

class ContactUsForm(forms.ModelForm):
    
    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'subject', 'message', )