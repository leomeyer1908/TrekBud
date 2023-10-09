"""
Name of File: travel/models.py
Brief description of the file: contains user model information to be stored in the database 
Inputs: None
Outputs: creates user class
"""


from django.db import models
from django.contrib.auth.models import User

#class for the user profile model
class UserProfile(models.Model):
	#retrives the user profile model from the data base
    user = models.OneToOneField(User, on_delete=models.CASCADE)
