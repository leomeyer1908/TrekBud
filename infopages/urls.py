# infopages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('about-us/', views.about_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('faqs/', views.faqs, name='faqs'),
]
