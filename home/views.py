from django.shortcuts import render


# Create your views here
def homepage(request):
    """
    returns the contact page
    """
    return render(request, 'home/homepage.html')


def contact(request):
    """
    returns the contact page
    """
    return render(request, 'home/contact.html')


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
    return render(request, 'home/plants.html')


def makeovers(request):
    """
    returns a page with examples of garden makeovers
    """
    return render(request, 'home/makeovers.html')