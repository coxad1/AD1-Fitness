import requests
import os
from dotenv import load_dotenv
from pydantic import ValidationError
from exercise import Exercise
from programManager import ProgramManager

load_dotenv("C:/Users/alexcox/Documents/GitHub/AD1-Fitness/.env")
exercise_db_api_key = os.getenv('API_KEY')

EXERCISEDB_BASE_URL = "https://exercisedb.p.rapidapi.com"
RAPID_API_HEADERS = {
    'x-rapidapi-key': exercise_db_api_key,
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

# Function to search exercises by name
def search_exr_by_name():
    name = input("What exercise would you like to search for? ")
    try:
        url = f"{EXERCISEDB_BASE_URL}/exercises/name/{name.lower()}"
        exercises = get_exercise_api(url)
        if exercises:
            for exercise in exercises:
                print(f"Found: {exercise['name']} - Target: {exercise['target']}")
        else:
            print("No exercises found.")
    except ValidationError as e:
        print(f"Error: {e}")

# Function to search exercises by body part
def search_exr_by_body_part():
    body_part = input("What body part would you like to target? ")
    url = f"{EXERCISEDB_BASE_URL}/exercises/bodyPart/{body_part.lower()}"
    exercises = get_exercise_api(url)
    if exercises:
        for exercise in exercises:
            print(f"Found: {exercise['name']} - Target: {exercise['target']}")
    else:
        print("No exercises found.")

# Function to search exercises by equipment used
def search_exr_by_equipment():
    equipment = input("What equipment would you like to use? ")
    url = f"{EXERCISEDB_BASE_URL}/exercises/equipment/{equipment.lower()}"
    exercises = get_exercise_api(url)
    if exercises:
        for exercise in exercises:
            print(f"Found: {exercise['name']} - Target: {exercise['target']}")
    else:
        print("No exercises found.")

# Function to search exercises by target muscle group
def search_exr_by_target_muscle():
    target = input("What muscle group would you like to target? ")
    url = f"{EXERCISEDB_BASE_URL}/exercises/target/{target.lower()}"
    exercises = get_exercise_api(url)
    if exercises:
        for exercise in exercises:
            print(f"Found: {exercise['name']} - Target: {exercise['target']}")
    else:
        print("No exercises found.")

# Exercise search menu
def search_exercise_menu():
    while True:
        print("""\nSearch Exercises
              \n 1. Search Exercises by Body Part
              \n 2. Search Exercises by Equipment
              \n 3. Search Exercises by Target
              \n 4. Search Exercises by Name
              \n 5. Back to Main Menu""")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            search_exr_by_body_part()
        elif choice == '2':
            search_exr_by_equipment()
        elif choice == '3':
            search_exr_by_target_muscle()
        elif choice == '4':
            search_exr_by_name()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

# Main menu
def main():
    program_manager = ProgramManager()  # Initialize Program Manager

    while True:
        print("""\n=== Main Menu ===
              \n 1. Manage Programs
              \n 2. Manage Workouts
              \n 3. Search Exercises
              \n 4. Exit""")

        choice = input("Enter your choice: ")

        if choice == '1':
            program_manager.manage_program_menu()  # Calls the Program Manager
        elif choice == '2':
            selected_program = program_manager.select_program()
            if selected_program:
                selected_program.program_menu()  # Calls the Workout menu for the selected program
            else:
                print("No programs available. Create a program first.")
        elif choice == '3':
            search_exercise_menu()  # Calls the exercise search menu
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
