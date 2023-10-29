"""
Name of File: accounts/urls.py
Brief description of the file: url for the accounts apps 
Inputs: None
Outputs: set url for the accounts apps
"""


from django.urls import path
from . import views

#url list for the accounts app
urlpatterns = [
	path('register/', views.registration, name='registration'), #set accounts/register to link to views.registration function
	path('confirm/<str:uidb64>/<str:token>/', views.confirm_email, name='confirm_email'), #set confirmation email to link to views.confirm email
    path('login/', views.loginUser, name="login"), #set login page to lead to loginUser function
	path('logout/', views.logoutUser, name="logout"), #set logout page to lead to logoutUser function
    path('update-user/', views.updateUser, name="updateUser"), #set logout page to lead to logoutUser function
    path('user-profile', views.userProfileAccount, name="userProfileAccount") #set user-profile page to point to userProfileAccount function 
]
