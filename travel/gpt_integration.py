"""
Name of File: travel/gpt_integration.py
Brief description of the file: gets information from the user, creates prompts for GPT, and sends back result from GPT model 
Inputs: information from user
Outputs: prompt from GPT model
"""

import openai

#main function is only used for testing, should be ignored otherwise
def main():
	option_list = ["interests", "budget", "climate", "activities", "cultural characteristics", "attractions", "transporation options", "dining options"]
	region_options = {}
	print("Enter the following preferences for regions (press Enter to skip):")
	for option in option_list:
		user_option = input(f"Enter {option}: ")
		if user_option.strip() != "":
			region_options[option] = user_option.strip().lower()
	
	display_regions_prompt = display_regions(region_options)

	regions = generate_text_with_gpt(display_regions_prompt)

	print(regions)
	
	"""
	locations = [string[17:] for string in regions.splitlines() if string[:13] == "Travel Region"]

	option_list = ["interests", "activity types", "do you want to visit museums?", "do you want to visit parks?", "do you want to visit landmarks?", "how popular should the places be?", "what should the ratings be?", "what proximity should they be from each other?"]
	attraction_options = {}
	print("Enter the following preferences for tourist attractions (press Enter to skip):")
	for option in option_list:
		user_option = input(f"Enter {option}: ")
		if user_option.strip() != "":
			region_options[option] = user_option.strip().lower()

	tourist_attractions = recommend_tourist_attraction(region, attraction_options)
	"""


#creates the prompt for displaying the regions based on the user preferences
def display_regions(user_options): 
	#starts prompt by telling GPT to list 3 regions with a criteria in a certain format
	prompt = """Suggest a list of the best 3 regions to travel to that match with the following criteria in the desired format:
Criteria:
###"""
	#for each user preference
	for option in user_options:
		#do a try block in case field is not a string, thus strip would not work
		try:
			#if the user typed in the preference
			if user_options[option].strip() != "":
				#add it to the prompt
				prompt += f"{option}: {user_options[option]}\n"
		#ignore if attribute error caused by strip
		except AttributeError:
			pass
	prompt += "###\n"

	#add the desired format GPT should use
	prompt += """Desired Format: 
	Travel Region 1: <City, Country>, <Explanation/Copywriting>
	Travel Region 2: <City, Country>, <Explanation/Copywriting>
	Travel Region 3: <City, Country>, <Explanation/Copywriting>"""

	#return the prompt
	return prompt


#creates the prompt for recommending tourist attractions based on the user preferences and the region
def recommend_tourist_attraction(region, user_options): 
	#start prompt by telling GPT to list 3 tourist attraction in a region with a criteria in a certain format
	prompt = f"Suggest a list of the best 3 tourist attractions in {region} that match with the following criteria:"
	prompt += """Criteria:
###"""
	#for each user preference
	for option in user_options:
		#do a try block in case field is not a string, thus strip would not work
		try:
			#if the user typed in the preference
			if user_options[option].strip() != "":
				#add it to the prompt
				prompt += f"{option}: {user_options[option]}\n"
		#ignore if attribute error caused by strip
		except AttributeError:
			pass
	prompt += "###\n"

	#add the desired format GPT should use
	prompt += """Desired Format: 
	Tourist Attraction 1: <Attraction Name> - <Explanation/Copywriting>
	Tourist Attraction 2: <Attraction Name> - <Explanation/Copywriting>
	Tourist Attraction 3: <Attraction Name> - <Explanation/Copywriting>"""


	#return the prompt
	return prompt

#creates the prompt for recommending tourist attractions based on the user preferences, the region, and attractions list
def generate_schedule(region, attractions, user_options):
	#start prompt by telling GPT to list 3 schedules in a region with the attractions with a criteria in a certain format
	prompt = f"Based on the following attractions: {', '.join(attractions)} for {region}, create a trip schedule that match with the following criteria:"
	prompt += """Criteria:
	###"""
	#for each user preference
	for option in user_options:
		#do a try block in case field is not a string, thus strip would not work
		try:
			#if the user typed in the preference
			if user_options[option].strip() != "":
				#add it to the prompt
				prompt += f"{option}: {user_options[option]}\n"
		#ignore if attribute error caused by strip
		except AttributeError:
			pass
	prompt += "###\n"

	#add the desired format GPT should use
	prompt += """Desired Format:
	Trip Schedule 1: <Attraction Name> - <Explanation/Copywriting>
		Day 1: 
		- 6AM-7AM: <what will be done during this time> 
		- 8AM-10AM: <what will be done during this time> 
		... <Include a detailed schedule like the one for Day 1 for all the days of the trip>
		Day <Day Num>:
		- <time>: <what will be done during this time> 
	
	Make sure to put all the days in between the first day and the last where it says "..." in the desired format, and do not skip any days.
	"""

	#return the prompt
	return prompt


#creates the prompt for recommending restaurants based on the user preferences, the region, and attractions list
def recommend_restaurant(region, user_options):
	#start prompt by telling GPT to list 3 restaurants in a region with a criteria in a certain format
	prompt = f"Suggest a list of 3 famous/popular restaurants in {region} that match with the following criteria:"
	prompt += """Criteria:###"""
	#for each user preference
	for option in user_options:
		#do a try block in case field is not a string, thus strip would not work
		try:
			#if the user typed in the preference
			if user_options[option].strip() != "":
				#add it to the prompt
				prompt += f"{option}: {user_options[option]}\n"
		#ignore if attribute error caused by strip
		except AttributeError:
			pass
	prompt += "###\n"

	#add the desired format GPT should use
	prompt += """Desired Format: 
	Restaurant 1: <Restaurant Name> - <Explanation/Copywriting>
	Restaurant 2: <Restaurant Name> - <Explanation/Copywriting>
	Restaurant 3: <Restaurant Name> - <Explanation/Copywriting>"""


	#return the prompt
	return prompt

	
	
#generate text from a prompt using GPT
def generate_text_with_gpt(input_text):
	#openai api key
	openai.api_key = "" 
	#Print that response is being generated to help debugging
	print("Generating GPT response...")
	#create a reponse from GPT
	response = openai.ChatCompletion.create(
		model="gpt-3.5-turbo", #use GPT 3.5
		messages=[
		{
			"role": "assistant", #user assistant role since we want it to help us
			"content": "Trip Planner. You are a trip planner and organizer. You know the best locations and tourist attractions in the world, and you are able to recommend the best places that someone should go based on their needs for them to have the best travel experience possible." #tell it that it is going to be a trip planner
		},
		{
			"role": "user", #this is our role, which is the user giving the message
			"content": input_text #this is the prompt
		}
		],
		temperature=1, #default variable for GPT which is not relevant for this project
		max_tokens=2048, #max token GPT is allowed to send back
		top_p=1, #default variable for GPT which is not relevant for this project
		frequency_penalty=0, #default variable for GPT which is not relevant for this project
		presence_penalty=0 # default variable for GPT which is not relevant for this project
	)

	#send back the contents of the message generated by GPT
	return response["choices"][0]["message"]["content"]

#if the file is called directly for testing
if __name__ == "__main__":
	#call main function
	main()
