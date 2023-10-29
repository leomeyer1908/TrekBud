"""
Name of File: accounts/models.py
Brief description of the file: create the user models for the user profile 
Inputs: None
Outputs: return the user profile models
"""


from django.contrib.auth.models import User
from django.db import models

#Create the user profile class to be stored in the database
class UserProfile(models.Model):
	#The following are all the fields that are saved for a user in the databse
    #The user field specifically inherits from the default Django user calss for things like username and password
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=20, unique=True, null=True)
    address = models.CharField(max_length=255, null=True)
    dietary_restrictions = models.CharField(max_length=255, null=True)
    emergency_contact = models.CharField(max_length=255, null=True)
    travel_style_preferences = models.CharField(max_length=255, null=True)
    preferred_airlines = models.CharField(max_length=255, null=True)
    budget_constraints = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    preferred_travel_dates = models.DateField(null=True)
    trip_duration = models.IntegerField(null=True)

    notification_preferences = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    profile_privacy = models.CharField(
        max_length=10,
        choices=[('private', 'Private'), ('public', 'Public')],
        default='public',
        null=True
    )
    #this specifies how the user should login. In this case, they use their username (as opposed to something like their email)
    USERNAME_FIELD = 'username'

	#overload the str class
    def __str__(self):
		#return the username for the class
        return self.user.username
    




