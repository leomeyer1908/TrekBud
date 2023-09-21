# accounts/views.py
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name for your home page
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})

