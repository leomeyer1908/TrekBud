"""
Name of File: accounts/forms.py
Brief description of the file: the forms used for the accounts registration form
Inputs: None
Outputs: Displays the account registration form
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

#create the registration form class that is used to get the form information of the users and inherits from Django's user creation form template
class RegistrationForm(UserCreationForm):
	#create username field
	username = forms.CharField(max_length=150, required=True, help_text="Required. 150 characters or fewer")
	#create a form for name
	name = forms.CharField(max_length=100, required=True, help_text="Required. 100 characters or fewer.")
	#create a form for email
	email = forms.EmailField(max_length=254, required=True, help_text="Required. Enter a valid email address.")
	#create a form for phone number
	phone_number = forms.CharField(max_length=20, required=True, help_text="Required. Enter your phone number.")
	#create a form for address
	address = forms.CharField(max_length=255, required=True, help_text="Required. Enter your address.")

	#create a form for diatary restrictions
	dietary_restrictions = forms.CharField(max_length=255, required=False, help_text="Specify dietary restrictions and preferences for dining recommendations.")
	#create a form for emergency contact
	emergency_contact = forms.CharField(max_length=255, required=False, help_text="Add emergency contact information for safety.")
	#create a form for travel style preferences
	travel_style_preferences = forms.CharField(max_length=255, required=False, help_text="Indicate travel style preferences (e.g., solo, family, adventure).")
	#create a form for prefereed airlines
	preferred_airlines = forms.CharField(max_length=255, required=False, help_text="Specify preferred airlines or hotel chains.")
	#create a form for budge constraints
	budget_constraints = forms.DecimalField(max_digits=10, decimal_places=2, required=False, help_text="Set budget constraints for travel recommendations.")

	#create a form for preferred travel dates
	preferred_travel_dates = forms.DateField(required=False, help_text="Select preferred travel dates.")
	#create a form for trip duration
	trip_duration = forms.IntegerField(required=False, help_text="Specify trip duration in days.")

		#notification choices that are given
	NOTIFICATION_CHOICES = (
		('email', 'Email'),
		('sms', 'SMS'),
		('push', 'Push Notifications'),
	)
	#create a multiple choice field for the notification choices form
	notification_preferences = forms.MultipleChoiceField(
		choices=NOTIFICATION_CHOICES,
		widget=forms.CheckboxSelectMultiple,
		required=False,
		help_text="Choose notification preferences during registration."
	)

	#create a profile picture form
	profile_picture = forms.ImageField(required=False, help_text="Upload a profile picture.")

	#allow profile picture to be set
	profile_privacy = forms.ChoiceField(
        choices=[('private', 'Private'), ('public', 'Public')],
        widget=forms.RadioSelect,
        required=False,
        help_text="Choose to keep the profile picture private or public."
    )

	#create a function to clean the data
	def clean(self):
		#get the cleaned data function from the inherited clean function
		cleaned_data = super().clean()
		#get the clean email function
		email = cleaned_data.get('email')
		#get the email confimation clean function
		email_confirmation = cleaned_data.get('email_confirmation')

		# Check if the email and email confirmation match
		if email and email_confirmation and email != email_confirmation:
			#give an error if the emails do not match
			raise forms.ValidationError("Email addresses do not match.")

	#create the meta class to display the forms
	class Meta:
		model = UserProfile
		#list the fields that will be displayed and the order in which they will appear
		fields = ['username', 'name', 'email', 'phone_number', 'address', 'password1', 'password2',
				  'dietary_restrictions', 'emergency_contact', 'travel_style_preferences',
				  'preferred_airlines', 'budget_constraints', 'preferred_travel_dates', 'trip_duration',
				  'notification_preferences', 'profile_picture', 'profile_privacy']

#create the forms for the user to be able to edit their profile, which just contains the same fields as registration
class UserProfileEditForm(forms.ModelForm):
	#edit username field
	username = forms.CharField(max_length=150, required=False, help_text="Required. 150 characters or fewer")
	#edit name field
	name = forms.CharField(max_length=100, required=False, help_text="Required. 100 characters or fewer.")
	#edit email field
	email = forms.EmailField(max_length=254, required=False, help_text="Required. Enter a valid email address.")
	#edit for phone number
	phone_number = forms.CharField(max_length=20, required=False, help_text="Required. Enter your phone number.")
	#edit address
	address = forms.CharField(max_length=255, required=False, help_text="Required. Enter your address.")

	#edit password field
	password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Leave this field empty to keep your current password'}),
        required=False,
    )
	#confirm the new password
	confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your new password'}),
        required=False,
    )

	#edit diatary restrictions
	dietary_restrictions = forms.CharField(max_length=255, required=False, help_text="Specify dietary restrictions and preferences for dining recommendations.")
	#edit emergency contact
	emergency_contact = forms.CharField(max_length=255, required=False, help_text="Add emergency contact information for safety.")
	#edit travel style preferences
	travel_style_preferences = forms.CharField(max_length=255, required=False, help_text="Indicate travel style preferences (e.g., solo, family, adventure).")
	#edit prefereed airlines
	preferred_airlines = forms.CharField(max_length=255, required=False, help_text="Specify preferred airlines or hotel chains.")
	#edit budge constraints
	budget_constraints = forms.DecimalField(max_digits=10, decimal_places=2, required=False, help_text="Set budget constraints for travel recommendations.")

	#edit preferred travel dates
	preferred_travel_dates = forms.DateField(required=False, help_text="Select preferred travel dates.")
	#edit trip duration
	trip_duration = forms.IntegerField(required=False, help_text="Specify trip duration in days.")

	#notification choices that are given
	NOTIFICATION_CHOICES = (
		('email', 'Email'),
		('sms', 'SMS'),
		('push', 'Push Notifications'),
	)
	#create a multiple choice field for the notification choices form
	notification_preferences = forms.MultipleChoiceField(
		choices=NOTIFICATION_CHOICES,
		widget=forms.CheckboxSelectMultiple,
		required=False,
		help_text="Choose notification preferences during registration."
	)

	#create a profile picture form
	profile_picture = forms.ImageField(required=False, help_text="Upload a profile picture.")

	#allow profile picture to be set
	profile_privacy = forms.ChoiceField(
        choices=[('private', 'Private'), ('public', 'Public')],
        widget=forms.RadioSelect,
        required=False,
        help_text="Choose to keep the profile picture private or public."
    )

	#create a function to clean the data
	def clean(self):
		#get the cleaned data function from the inherited clean function
		cleaned_data = super().clean()
		#get the clean email function
		email = cleaned_data.get('email')
		#get the email confimation clean function
		email_confirmation = cleaned_data.get('email_confirmation')

		# Check if the email and email confirmation match
		if email and email_confirmation and email != email_confirmation:
			#give an error if the emails do not match
			raise forms.ValidationError("Email addresses do not match.")
		
		#get the cleaned password
		password = cleaned_data.get('password')
		#get the confirmed clean passowrd
		confirm_password = cleaned_data.get('confirm_password')

        # Check if both password and confirm_password are provided
		if password and confirm_password:
			#if the password does not match with the confirmed password
			if password != confirm_password:
				#say that the passwords do not match
				raise forms.ValidationError("Passwords do not match.")
		#if only one of the fields are filled in
		elif password or confirm_password:
			#raise an error by saying both fields need to be filled in
			raise forms.ValidationError("Both password fields are required when changing the password.")


	#create the meta class to display the forms
	class Meta:
		#user model that is used is the custom user model we created with the custom fields
		model = UserProfile
		#list the fields that will be displayed and the order in which they will appear
		fields = ['username', 'name', 'email', 'phone_number', 'address', 'password', 'confirm_password',
				  'dietary_restrictions', 'emergency_contact', 'travel_style_preferences',
				  'preferred_airlines', 'budget_constraints', 'preferred_travel_dates', 'trip_duration',
				  'notification_preferences', 'profile_picture', 'profile_privacy']