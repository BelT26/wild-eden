from django.urls import path
from . import views

urlpatterns = [    
    path('', views.homepage, name='home'),
    path('faqs', views.faqs, name='faqs'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('makeovers', views.makeovers, name='makeovers'),
    path('plants', views.plants, name='plants'),
    path('gallery', views.gallery, name='gallery')
]