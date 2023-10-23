"""
Name of File: home/views.py
Brief description of the file: set function that executes when loading home page
Inputs: None
Outputs: loads home page
"""

from django.shortcuts import render


#function that runs when home page is requested
def home(request):
    #returns the home.html template
    return render(request, 'home.html', {})
