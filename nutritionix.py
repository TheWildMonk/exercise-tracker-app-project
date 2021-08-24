# Import required libraries
import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv("/Volumes/Workstation/Learning Center/Data Science/"
            "100 Days of Code - Complete Python Pro Bootcamp 2021/Projects/@CREDENTIALS/.env")


# Nutritionix API Class
class Nutritionix:
    """Class representing all functionalities of Nutritionix API"""
    def __init__(self, query: str, gender: str, weight_kg: float, height_cm: float, age: int):
        self.query = query
        self.gender = gender
        self.weight_kg = weight_kg
        self.height_cm = height_cm
        self.age = age
        self.ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
        self.HEADER = {
            "x-app-id": os.getenv("NUTRITIONIX_APP_ID"),
            "x-app-key": os.getenv("NUTRITIONIX_API_KEY"),
            "x-remote-user-id": "0",
        }
        self.PARAMS = {
            "query": self.query,
            "gender": self.gender,
            "weight_kg": self.weight_kg,
            "height_cm": self.height_cm,
            "age": self.age,
        }

    def post_response(self):
        """Function to post NLP data to Nutritionix
        for retrieval of required data, e.g. name of the exercise,
        duration of the exercise performed & total calories burned
        through the exercise."""
        nx_post = requests.post(url=self.ENDPOINT, json=self.PARAMS, headers=self.HEADER)
        return nx_post
