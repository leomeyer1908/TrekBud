from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
	name = forms.CharField(max_length=100, required=True, help_text="Required. 100 characters or fewer.")
	email = forms.EmailField(max_length=254, required=True, help_text="Required. Enter a valid email address.")
	phone_number = forms.CharField(max_length=20, required=True, help_text="Required. Enter your phone number.")
	address = forms.CharField(max_length=255, required=True, help_text="Required. Enter your address.")

	dietary_restrictions = forms.CharField(max_length=255, required=False, help_text="Specify dietary restrictions and preferences for dining recommendations.")
	emergency_contact = forms.CharField(max_length=255, required=False, help_text="Add emergency contact information for safety.")
	travel_style_preferences = forms.CharField(max_length=255, required=False, help_text="Indicate travel style preferences (e.g., solo, family, adventure).")
	preferred_airlines = forms.CharField(max_length=255, required=False, help_text="Specify preferred airlines or hotel chains.")
	budget_constraints = forms.DecimalField(max_digits=10, decimal_places=2, required=False, help_text="Set budget constraints for travel recommendations.")

	preferred_travel_dates = forms.DateField(required=False, help_text="Select preferred travel dates.")
	trip_duration = forms.IntegerField(required=False, help_text="Specify trip duration in days.")
	
	NOTIFICATION_CHOICES = (
		('email', 'Email'),
		('sms', 'SMS'),
		('push', 'Push Notifications'),
	)
	notification_preferences = forms.MultipleChoiceField(
		choices=NOTIFICATION_CHOICES,
		widget=forms.CheckboxSelectMultiple,
		required=False,
		help_text="Choose notification preferences during registration."
	)

	profile_picture = forms.ImageField(required=False, help_text="Upload a profile picture.")

	profile_privacy = forms.ChoiceField(
        choices=[('private', 'Private'), ('public', 'Public')],
        widget=forms.RadioSelect,
        required=False,
        help_text="Choose to keep the profile picture private or public."
    )

	email2 = forms.EmailField(
		label="Confirm Email",
		required=True,
		help_text="Enter the same email address as above, for verification."
	)

	def clean(self):
		cleaned_data = super().clean()
		email = cleaned_data.get('email')
		email_confirmation = cleaned_data.get('email_confirmation')

		# Check if the email and email confirmation match
		if email and email_confirmation and email != email_confirmation:
			raise forms.ValidationError("Email addresses do not match.")

	class Meta:
		model = User
		fields = ['username', 'name', 'email', 'email2', 'phone_number', 'address', 'password1', 'password2',
				  'dietary_restrictions', 'emergency_contact', 'travel_style_preferences',
				  'preferred_airlines', 'budget_constraints', 'preferred_travel_dates', 'trip_duration',
				  'notification_preferences', 'profile_picture', 'profile_privacy']
