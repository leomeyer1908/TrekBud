"""
Name of File: trekbud/urls.py
Brief description of the file: all the urls for the apps
Inputs: None
Outputs: connects all the URLS for the apps
"""
from django.contrib import admin
from django.urls import path, include  # Import the 'include' function

#list of the urls for the website
urlpatterns = [
    path('admin/', admin.site.urls), #admin url
    path('', include('home.urls')), #home url
    path('accounts/', include('accounts.urls')), #get the accounts url from accounts/accounts.urls
    path('travel/', include('travel.urls')), # get the travel url from travel/travel.urls
    # Add other app URLs here
]

