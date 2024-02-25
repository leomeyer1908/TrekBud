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
		fields = ['user', 'name', 'email', 'phone_number', 'address', 'password1', 'password2',
				  'dietary_restrictions', 'emergency_contact', 'travel_style_preferences',
				  'preferred_airlines', 'budget_constraints', 'preferred_travel_dates', 'trip_duration',
				  'notification_preferences', 'profile_picture', 'profile_privacy']
