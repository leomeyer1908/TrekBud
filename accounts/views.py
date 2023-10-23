"""
Name of File: accounts/views.py
Brief description of the file: the functions that the user will view for the accounts pages 
Inputs: None
Outputs: display the proper html templates on the user's browsers
"""


from django.contrib.auth import login, authenticate, get_user_model, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.utils import IntegrityError



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
			try:
				with transaction.atomic():
					# Create a User instance for authentication
					user = User.objects.create_user(
						username=form.cleaned_data.get('username'),
						password=form.cleaned_data.get('password1'),
						email=form.cleaned_data.get('email')
					)

					# Create a UserProfile instance and populate it with form data
					user_profile = UserProfile.objects.create(
						user=user,
						name=form.cleaned_data.get('name'),
						email=form.cleaned_data.get('email'),
						phone_number=form.cleaned_data.get('phone_number'),
						address=form.cleaned_data.get('address'),
						dietary_restrictions=form.cleaned_data.get('dietary_restrictions'),
						emergency_contact=form.cleaned_data.get('emergency_contact'),
						travel_style_preferences=form.cleaned_data.get('travel_style_preferences'),
						preferred_airlines=form.cleaned_data.get('preferred_airlines'),
						budget_constraints=form.cleaned_data.get('budget_constraints'),
						preferred_travel_dates=form.cleaned_data.get('preferred_travel_dates'),
						trip_duration=form.cleaned_data.get('trip_duration'),
						notification_preferences=', '.join(form.cleaned_data.get('notification_preferences')),
						profile_picture=form.cleaned_data.get('profile_picture'),
						profile_privacy=form.cleaned_data.get('profile_privacy'),
					)

					#save the user profile information to the database
					user_profile.save()

					#get cleaned username
					username = form.cleaned_data.get('username')
					#get cleaned password
					password = form.cleaned_data.get('password1')
					#authenticate the user based on their new username and password, so user is automatically logged in
					user = authenticate(username=username, password=password)
					#login with the proper user authentication
					login(request, user)
					#send the user to be on the home page
					return redirect('home')  # Replace 'home' with the URL name for your home page
			except IntegrityError as e:
				form.add_error(None, "Username or email is already taken.")
	#if the user has not submit the form yet
	else:
		#load the registration page 
		form = RegistrationForm()
	#send the template of the registration page html along with the forms for it to be displayed on the user's browser
	return render(request, 'registration/registration.html', {'form': form})

#function to login user
def loginUser(request):
	#if the user submits the login form
	if request.method == 'POST':
		#get the username that was submitted
		username = request.POST.get('username')
		#get the password that was submitted
		password = request.POST.get('password')
		
		#try to login with the given credentials
		user = authenticate(request, username=username, password=password)

		#if the user exists
		if user is not None:
			#login the user
			login(request, user)
			#send them back to the home page afterwards
			return redirect('home')
		else:
			print("User does not exist")

	#send the template of the login.html page for the login
	return render(request, 'login/login.html', {})


#Function that runs when user logouts
def logoutUser(request):
	#logs out the user
	logout(request)
	#sends user back to the home page
	return redirect('home')

#make login required to update the user
@login_required(login_url='login')
#add the update user function
def updateUser(request):
	#send the template of the update_user.html page when the user wants to update their information
	return render(request, "update_user/update_user.html")

#This function gets called to create the user profile account page
def userProfileAccount(request):
	# Check if the user is authenticated
    if request.user.is_authenticated:
		#print which user is authenticated on terminal for debugging
        print(f"User {request.user.username} is authenticated.")
        # Get the user's profile based on the currently logged-in user
        user_profile = UserProfile.objects.get(user=request.user)
		#update context with the new user profile, so that it gets sent to the browser
        context = {'userProfile': user_profile}
		#load the user profile page, with the context of the current user profile
        return render(request, 'profile/user_profile.html', context)
    else:
        # Handle the case where the user is not authenticated by sending them to login
        return redirect('login')