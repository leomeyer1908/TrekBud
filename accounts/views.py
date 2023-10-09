"""
Name of File: accounts/views.py
Brief description of the file: the functions that the user will view for the accounts pages 
Inputs: None
Outputs: display the proper html templates on the user's browsers
"""


from django.contrib.auth import login, authenticate, get_user_model
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

#function that sends a confirmation email when user signs up
def send_confirmation_email(request, user):
	#ge tthe current website
	current_site = get_current_site(request)
	#subject used on email
	mail_subject = 'Confirm your email address'
	#get the tokens for the user to send the correct email
	token = default_token_generator.make_token(user)
	#get the user uuid to send the email to the correct user
	uid = urlsafe_base64_encode(force_bytes(user.pk))
	#send the confirmation url to the proper user email
	confirmation_url = reverse('confirm_email', args=[uid, token])
	#the message to be sent which there is a preset from django
	message = render_to_string('registration/confirmation_email.html', {
		'user': user,
		'domain': current_site.domain,
		'confirmation_url': confirmation_url,
	})
	#send the email
	send_mail(mail_subject, message, 'your_email@gmail.com', [user.email])
	#tell the user that the confirmation email was send
	return render(request, 'registration/email_confirmation_sent.html')

#check if the user confirmed their email
def confirm_email(request, uidb64, token):
	#get the user class
	User = get_user_model()
	try:
		#get the id of the user
		uid = urlsafe_base64_decode(uidb64).decode()
		#get the user
		user = User.objects.get(pk=uid)
	#if there is an error
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		#say that the user is none
		user = None

	#if the user exist or they confirmed email
	if user and default_token_generator.check_token(user, token):
		#save on the user information that they confirmed their email
		user.email_confirmed = True
		#save the user data onto the database
		user.save()
		#send a page to the user email that it is confirmed
		return render(request, 'registration/email_confirmed.html')
	#if the user does not exist or they did not confirm email
	else:
		#send the user an html page saying that they did confirm the email	
		return render(request, 'registration/invalid_confirmation_link.html')

#make the user registration page form
def registration(request):
	#if the user submits the form
	if request.method == 'POST':
		#get the form for the user registration
		form = RegistrationForm(request.POST)
		#if the form has no error
		if form.is_valid():
			#set the user to have the information from the form
			user = form.save()
			#clean the data for the username
			username = form.cleaned_data.get('username')
			#clean the data for the password
			password = form.cleaned_data.get('password1')
			#authenticate the user based on their new username and password
			user = authenticate(username=username, password=password)
			#lgoin with the proper user authentication
			login(request, user)
			#send the user to be on the home page
			return redirect('home')  # Replace 'home' with the URL name for your home page
	#if the user has not submit the form yet
	else:
		#load the registration page 
		form = RegistrationForm()
	#send the template of the registration page html along with the forms for it to be displayed on the user's browser
	return render(request, 'registration/registration.html', {'form': form})

