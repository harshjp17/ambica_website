from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EnquiryForm

def home(request):
    return render(request, 'main/home.html', {'page': 'home'})

def services(request):
    return render(request, 'main/services.html', {'page': 'services'})

def about(request):
    return render(request, 'main/about.html', {'page': 'about'})

def contact(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your enquiry has been submitted. We will contact you within 24 hours.')
            return redirect('contact')
    else:
        form = EnquiryForm()
    return render(request, 'main/contact.html', {'page': 'contact', 'form': form})
