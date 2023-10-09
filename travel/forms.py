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
	#list of all the options
	option_list = ["interests", "activity_types", "do_you_want_to_visit_museums?", "do_you_want_to_visit_parks?", "do_you_want to_visit_landmarks?", "how_popular_should_the_places_be?", "what_should_the_ratings_be?", "what_proximity_should_they_be_from each_other?"]

	# Create a form field for each of the personalized user settings
	interests = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer.")
	activity_types = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer.")
	museums = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer.")
	parks = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer.")
	landmarks = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer.")
	popular = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer.")
	ratings = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer.")
	proximity = forms.CharField(max_length=100, required=False, help_text="100 characters or fewer.")


#create the Meta for the tourist attractions to be able to display the forms
class TouristAttractionFormMeta:
	#create Meta class
    class Meta:
		#get the fields to be displayed from the tourist attractions form
        fields = TouristAttractionForm.option_list

#set the region selection meta to be the tourist attractions meta class
TouristAttractionForm.Meta = TouristAttractionFormMeta



#create the forms for the generate schedule page page
class GenerateScheduleForm(forms.Form):
	#list of all the options
	option_list = ["date", "time", "duration"]

	# Create a form field for each of the personalized user settings
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
