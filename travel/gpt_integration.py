import openai
if __name__ != "__main__":
	from django.conf import settings 


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


	

def display_regions(user_options): 
	prompt = """Suggest a list of the best 3 regions to travel to that match with the following criteria in the desired format:
	Criteria:
	###"""
	for option in user_options:
		prompt += f"{option}: user_options\n"
	prompt = "###\n"

	prompt = """Desired Format: ###
	Travel Region 1: <City, Country>, <Explanation/Copywriting>
	Travel Region 2: <City, Country>, <Explanation/Copywriting>
	Travel Region 3: <City, Country>, <Explanation/Copywriting>###"""

	return prompt


		
def recommend_tourist_attraction(region, user_options): 
	prompt = """Suggest a list of the best 3 tourist attractions in {region} that match with the following criteria:
	Criteria:
	###"""
	for option in user_options:
		prompt += f"{option}: user_options\n"
	prompt = "###\n"

	prompt = """Desired Format: ###
	Tourist Attraction 1: <Attraction Name> - <Explanation/Copywriting>
	Tourist Attraction 2: <Attraction Name> - <Explanation/Copywriting>
	Tourist Attraction 3: <Attraction Name> - <Explanation/Copywriting>###"""


	return prompt

def generate_schedule(region, attractions, user_options):
	prompt = """Based on the following attractions: {", ".join(attractions)} for {region}, create 3 trip schedules that match with the following criteria:
	Criteria:
	###"""
	for option in user_options:
		prompt += f"{option}: user_options\n"
	prompt = "###\n"

	prompt = """Desired Format: ###
	Trip Schedule 1:
		- 6AM-7AM: <what will be done during this time> 
		- 8AM-10AM: <what will be done during this time> 
		...
		- <time>: <what will be done during this time> 
	Trip Schedule 2: <Attraction Name> - <Explanation/Copywriting>
		- 8AM-9AM: <what will be done during this time> 
		...
		- <time>: <what will be done during this time> 
	Trip Schedule 3: 
		- <time>: <what will be done during this time> 
		...
		- <time>: <what will be done during this time> 
	###"""

	return prompt

	
	

def generate_text_with_gpt(input_text):
    #openai.api_key = settings.OPENAI_API_KEY 
	response = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=[
		{
			"role": "assistant",
			"content": "Trip Planner. You are a trip planner and organizer. You know the best locations and tourist attractions in the world, and you are able to recommend the best places that someone should go based on their needs for them to have the best travel experience possible."
		},
		{
			"role": "user",
			"content": input_text
		}
		],
		temperature=1,
		max_tokens=2048,
		top_p=1,
		frequency_penalty=0,
		presence_penalty=0
	)

	return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
	main()
