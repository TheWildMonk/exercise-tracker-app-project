# Import required modules
from nutritionix import Nutritionix
from sheety import Sheety

# Ask user for the exercises they did for the day
user_query = input("Which exercises have you performed today: ")

# Create Nutritionix Object & post the data for retrieving
# name of exercises, performed duration & total calories burned
nx_object = Nutritionix(query=user_query, gender="male", weight_kg=86.7, height_cm=175.26, age=31)
nx_post_data = nx_object.post_response()

# For loop to loop through each exercise
for key in range(0, len(nx_post_data.json()["exercises"])):
    # Create Sheety object and post the data to google sheets
    sheety_object = Sheety(exercise=nx_post_data.json()["exercises"][key]["name"].title(),
                           duration=nx_post_data.json()["exercises"][key]["duration_min"],
                           calories=nx_post_data.json()["exercises"][key]["nf_calories"])
    sheety_post_response = sheety_object.post_response()
    print(sheety_post_response.text)
