"""
Name of File: travel/forms.py
Brief description of the file: create the forms forms for all the travel recommendation pages 
Inputs: None
Outputs: send the forms to the user for the proper travel recommendation pages
"""
from django import forms

#create the forms for the region selection page
class RegionSelectionForm(forms.Form):
	#list of all the options
	option_list = [
		"interests", "budget", "climate", "activities",
		"cultural_characteristics", "attractions", 
		"transportation_options", "dining_options"
	]
	
	# Create a form field for each of the personalized user settings
	interests = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer.")
	budget = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer.")
	climate = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer.")
	activities = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer.")
	cultural_characteristics = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer.")
	attractions = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer.")
	transportation_options = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer.")
	dining_options = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer.")


#create the Meta for the region selection to be able to display the forms
class RegionSelectionFormMeta:
	#create Meta class
    class Meta:
		#get the fields to be displayed from the region selection form
        fields = RegionSelectionForm.option_list

#set the region selection meta to be the region selection meta class
RegionSelectionForm.Meta = RegionSelectionFormMeta


#create the forms for the tourist attractions page
class TouristAttractionForm(forms.Form):
    # Create a form field for each of the personalized user settings
    region = forms.CharField(max_length=100, required=True, help_text="100 characters or fewer", label="Enter region you would like to travel to")
    interests = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer", label="Do you have any specific interests?")
    activity_types = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer", label="What types of activities do you enjoy?")
    museums = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer", label="Do you want to visit museums?")
    parks = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer", label="Do you want to visit parks?")
    landmarks = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer", label="Do you want to visit landmarks?")
    popular = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer", label="How popular should the places be?")
    ratings = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer", label="What should the ratings be?")
    proximity = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer", label="What proximity should they be from each other?")

	#create Meta class
    class Meta:
        #get the fields to be displayed from the tourist attractions form
        fields = ['region', 'interests', 'activity_types', 'museums', 'parks', 'landmarks', 'popular', 'ratings', 'proximity']
        


#create the forms for the generate schedule page page
class GenerateScheduleForm(forms.Form):
	#list of all the options
	option_list = ["date", "time", "duration"]

	# Create a form field for each of the personalized user settings
	region = forms.CharField(max_length=100, required=True, help_text="100 characters or fewer", label="Enter region you would like to travel to")
	attractions = forms.CharField(max_length=100, required=True, help_text="100 characters or fewer", label="Enter at least one attraction you would like to visit")
	date = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer.")
	time = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer.")
	duration = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer.")


#create the Meta for the generate schedule to be able to display the forms
class GenerateScheduleFormMeta:
	#create Meta class
    class Meta:
		#get the fields to be displayed from the generate schedule form
        fields = GenerateScheduleForm.option_list

#set the generate schedule meta to be the tourist attractions meta class
GenerateScheduleForm.Meta = GenerateScheduleFormMeta

#create the forms for the tourist attractions page
class RecommendRestaurantsForm(forms.Form):
    # Create a form field for each of the personalized user settings
    region = forms.CharField(max_length=100, required=True, help_text="100 characters or fewer", label="Enter region you would like to travel to")
    cuisine_preferences = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer", label="Enter your cuisine preferences")
    dietary_restrictions = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer", label="Enter your dietary restrictions")
    price_range = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer", label="What is your desired price range?")
    min_rating = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer", label="Enter the minimum rating for the restaurant")
    max_distance = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer", label="Enter the maximum distance you and the restaurants")

	#create Meta class
    class Meta:
        #get the fields to be displayed from the tourist attractions form
        fields = ['region', 'cuisine_preferences', 'dietary_restrictions', 'price_range', 'min_rating', 'max_distance']
        

#this is the formes for the weather selection
class WeatherForm(forms.Form):
    region = forms.CharField(label='Region (City)', max_length=100)
    travel_duration = forms.IntegerField(label='Travel Duration (hours)')
