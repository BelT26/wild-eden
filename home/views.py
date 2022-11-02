from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .models import Plant


# Create your views here
def homepage(request):
    """
    returns the home page
    """
    return render(request, 'home/homepage.html')


def contact(request):
    """
    returns the contact page
    """
    return render(request, 'home/contact.html')


def contactform(request):
    """
    returns the a page with a contact form
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry" 
            body = {
                'full_name': form.cleaned_data['full_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
                }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['helen.taylor@hotmail.it']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("home")    
    form = ContactForm()
    return render(request, "home/contact.html", {'form': form})


def services(request):
    """
    returns the services page
    """
    return render(request, 'home/services.html')


def faqs(request):
    """
    returns the faqs page
    """
    return render(request, 'home/faqs.html')


def plants(request):
    """
    returns a page with a list of available plants
    """
    all_plants = Plant.objects.all()
    return render(request, 'home/plants.html', {'plants': all_plants})


def makeovers(request):
    """
    returns a page with examples of garden makeovers
    """
    return render(request, 'home/makeovers.html')

def gallery(request):
    """
    returns a view of the gallery
    """
    return render(request, 'home/gallery.html')