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
	#create the user profile 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')

	#store the picture in the database
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

	#overload the str class
    def __str__(self):
		#return the username for the class
        return self.user.username
