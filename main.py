import requests
import os
from pydantic import BaseModel, ValidationError, HttpUrl
from dotenv import load_dotenv
from typing import List

load_dotenv('/Users/alexcox/Documents/GitHub/AD1-Fitness/.env')
api_key = os.getenv('API_KEY')

# Base URL for ExerciseDB API
EXERCISEDB_BASE_URL = "https://exercisedb.p.rapidapi.com"

# Replace with your actual headers for API access
RAPID_API_HEADERS = {
    'x-rapidapi-key': 'api_key',
    'x-rapidapi-host': 'exercisedb.p.rapidapi.com'
}
# Placeholder for the current workout being built
current_workout = []

# Pydantic model for Exercise
class Exercise(BaseModel):
    bodyPart: str
    equipment: str
    gifUrl: HttpUrl
    id: str
    name: str
    target: str
    secondaryMuscles: List[str]
    instructions: List[str]

def ping_exercisedb_api(url):
    try:
        response = requests.get(url, headers=RAPID_API_HEADERS)
        
        if response.status_code == 200:
            try:
                data = response.json()
                print("API status: Online")
                return data
            except ValueError as json_error:
                print(f"Failed to parse JSON: {json_error}")
                return None
        else:
            print(f"Failed request. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

# Main function to create a new workout
def create_new_workout():
    print("Creating a new workout")
    search_for_exercises()

# Function to search for exercises
def search_for_exercises():
    print("Choose how you would like to search for exercises:")
    print("1. By Exercise Name")
    print("2. By Body Part")
    print("3. By Equipment Used")
    print("4. By Target Muscle Group")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter exercise name: ")
        search_by_exercise_name(name)
    elif choice == '2':
        body_part = input("Enter body part: ")
        search_by_body_part(body_part)
    elif choice == '3':
        equipment = input("Enter equipment used: ")
        search_by_equipment(equipment)
    elif choice == '4':
        target = input("Enter target muscle group: ")
        search_by_target_muscle(target)
    else:
        print("Invalid choice. Please try again.")
        search_for_exercises()

# Function to search exercises by name
def search_by_exercise_name(name):
    url = f"{EXERCISEDB_BASE_URL}/exercises/name/{name}"
    exercises = ping_exercisedb_api(url)
    if exercises:
        validate_and_display_exercises(exercises)

# Function to search exercises by body part
def search_by_body_part(body_part):
    url = f"{EXERCISEDB_BASE_URL}/exercises/bodyPart/{body_part}"
    exercises = ping_exercisedb_api(url)
    if exercises:
        validate_and_display_exercises(exercises)

# Function to search exercises by equipment used
def search_by_equipment(equipment):
    url = f"{EXERCISEDB_BASE_URL}/exercises/equipment/{equipment}"
    exercises = ping_exercisedb_api(url)
    if exercises:
        validate_and_display_exercises(exercises)

# Function to search exercises by target muscle group
def search_by_target_muscle(target):
    url = f"{EXERCISEDB_BASE_URL}/exercises/target/{target}"
    exercises = ping_exercisedb_api(url)
    if exercises:
        validate_and_display_exercises(exercises)

# Validate and display exercises using Pydantic
def validate_and_display_exercises(exercises: List[dict]):
    print("\nExercises Found:")
    for i, exercise_data in enumerate(exercises, start=1):
        try:
            exercise = Exercise(**exercise_data)
            print(f"{i}. {exercise.name}")
            print(f"   - Body Part: {exercise.bodyPart}")
            print(f"   - Equipment: {exercise.equipment}")
            print(f"   - Target Muscle: {exercise.target}")
            print(f"   - GIF URL: {exercise.gifUrl}")

        except ValidationError as e:
            print(f"Error validating exercise data: {e}")
        
# Function to add selected exercise to the current workout
def add_exercise_to_workout(exercise):
    # This could be stored locally or in a list
    current_workout.append(exercise)
    print(f"{exercise['name']} added to your workout.")

# Function to modify an existing workout
def modify_existing_workout():
    print("Loading existing workout...")
    # Load from saved file or session
    load_workout()

def load_workout():
    # Simulate loading a workout (from file, db, etc.)
    pass

# Function to customize the weekly workout plan
def customize_weekly_workout_plan():
    print("Customizing weekly workout plan...")
    # Customization logic (sets, reps, etc.)
    pass

# Function to export the workout plan
def export_workout_plan():
    print("Exporting workout plan...")
    # Create export format
    export_to_txt(current_workout)

def export_to_txt(workout):
    with open('workout_plan.txt', 'w') as f:
        for exercise in workout:
            f.write(f"{exercise['name']} - {exercise['sets']} sets, {exercise['reps']} reps\n")
    print("Workout plan exported to workout_plan.txt")

# Main entry point for the application
if __name__ == "__main__":
        print("Welcome to the Workout Plan App!")
        create_new_workout()  