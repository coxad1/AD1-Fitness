import requests
import os
from dotenv import load_dotenv
from typing import List
from pydantic import ValidationError
from exercise import search_exercise_menu, bodyPartTarget, equipmentUsed, targetMuscle
from workout import Workout, workout_menu

load_dotenv("C:/Users/alexcox/Documents/GitHub/AD1-Fitness/.env")
api_key = os.getenv('API_KEY')
workouts: List[Workout] = []
EXERCISEDB_BASE_URL = "https://exercisedb.p.rapidapi.com"
RAPID_API_HEADERS = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': 'exercisedb.p.rapidapi.com'
}

# Helper function to make standardized API requests with error handling
def get_exercise_api(url):
    try:
        response = requests.get(url, headers=RAPID_API_HEADERS)
        response.raise_for_status()  # Raise an HTTPError if the response was unsuccessful

        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

# Function to check API status before proceeding
def check_api_status():
    url = f"{EXERCISEDB_BASE_URL}/status"
    result = get_exercise_api(url)
    if result:
        print("API status: Online")
        return True
    else:
        print("API status: Unavailable.")
        return False

# Function to search exercises by name
def search_exr_by_name(name):
    name = input("What exercise would you like to search for?")
    try:
        name = name.lower()
        url = f"{EXERCISEDB_BASE_URL}/exercises/name/{name}"
        exercises = get_exercise_api(url)
        if exercises:
            return exercises
    except ValidationError as e:
        print(f"Not found")

# Function to search exercises by body part
def search_exr_by_body_part(body_part):
    body_part = input("What body part would you like to target?")
    if body_part in bodyPartTarget:
        url = f"{EXERCISEDB_BASE_URL}/exercises/bodyPart/{body_part}"
        exercises = get_exercise_api(url)
        if exercises:
            return exercises

# Function to search exercises by equipment used
def search_exr_by_equipment(equipment):
    equipment = input("What equipment would you like to use?")
    if equipment in equipmentUsed:
        url = f"{EXERCISEDB_BASE_URL}/exercises/equipment/{equipment}"
        exercises = get_exercise_api(url)
        if exercises:
            return exercises
  
# Function to search exercises by target muscle group
def search_exr_by_target_muscle(target):
    target = input("What muscle group would you like to target?")
    if target in targetMuscle:
        url = f"{EXERCISEDB_BASE_URL}/exercises/target/{target}"
        exercises = get_exercise_api(url)
        if exercises:
            return exercises
