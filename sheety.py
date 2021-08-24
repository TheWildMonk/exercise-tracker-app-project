# Import required libraries
import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load .env file
load_dotenv("/Volumes/Workstation/Learning Center/Data Science/"
            "100 Days of Code - Complete Python Pro Bootcamp 2021/Projects/@CREDENTIALS/.env")


# Sheety API class
class Sheety:
    """Class representing all functionalities of Sheety API"""
    def __init__(self, exercise: str, duration: float, calories: float):
        self.exercise = exercise
        self.duration = duration
        self.calories = calories
        self.today_date = datetime.today().date().strftime("%d/%m/%Y")
        self.time_now = datetime.now().time().strftime("%X")
        self.API_KEY = os.getenv("SHEETY_API_KEY")
        self.ENDPOINT = f"https://api.sheety.co/{self.API_KEY}/workoutTracking/workouts"
        self.PARAMS = {
            "workout": {
                "date": self.today_date,
                "time": self.time_now,
                "exercise": self.exercise,
                "duration": self.duration,
                "calories": self.calories,
            }
        }

    def post_response(self):
        """Function to Post workout data to google sheets"""
        sheety_post = requests.post(url=self.ENDPOINT, json=self.PARAMS)
        return sheety_post
