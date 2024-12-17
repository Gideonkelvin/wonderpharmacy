from django.shortcuts import render, redirect
from core.forms import ContactUsForm
from core.utils import EmailService

# Create your views here.
def home(request):
    return render(request, 'index.html')

def add_contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid:
            c =form.save()
            EmailService.send_contact_form_emails(
                contact=c
            )
    return redirect('index')

