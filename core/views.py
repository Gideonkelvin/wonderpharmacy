from django.shortcuts import render, redirect
from core.forms import ContactUsForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def add_contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid:
            form.save()
    return redirect('index')

