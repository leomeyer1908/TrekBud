"""
Name of File: accounts/urls.py
Brief description of the file: url for the accounts apps 
Inputs: None
Outputs: set url for the accounts apps
"""


from django.urls import path
from . import views

#url list for the accounts app
urlpatterns = [
    path('', views.home, name='home'), #link the default link to home function
	path('home/', views.home, name='home'), #link home page to home function
]
