import requests
import os
from dotenv import load_dotenv
from pydantic import ValidationError
from exercise import Exercise
from programManager import ProgramManager
from workout import Workout

bodyPartTarget = ["back", "cardio", "chest", "lower arms", "lower legs", "neck", "shoulders", "upper arms", "upper legs", "waist"]
equipmentUsed = ["assisted", "band", "barbell", "body weight", "bosu ball", "cable", "dumbbell", "elliptical machine", "ez barbell", "hammer", "kettlebell", "leverage machine", "medicine ball", "olympic barbell", "resistance band", "roller", "rope", "skierg machine", "sled machine", "smith machine", "stability ball", "stationary bike", "stepmill machine", "tire", "trap bar", "upper body ergometer", "weighted", "wheel roller"]
targetMuscle = ["abductors", "abs", "adductors", "biceps", "calves", "cardiovascular system", "delts", "forearms", "glutes", "hamstrings", "lats", "levator scapulae", "pectorals", "quads", "serratus anterior", "spine", "traps", "triceps", "upper back"]

load_dotenv()
exercise_db_api_key = os.getenv('API_KEY')
print(exercise_db_api_key)
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
    url = f"{EXERCISEDB_BASE_URL}/exercises/name/{name.lower()}"
    exercises = get_exercise_api(url)
    for exercise in exercises:
            print(f"Found: {exercise['name']} - Target: {exercise['target']}")
    else: print("No exercises found.")

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
            for body_part in bodyPartTarget:
                print(body_part.capitalize())
            search_exr_by_body_part()
        elif choice == '2':
            for equipment in equipmentUsed:
                print(equipment.capitalize())
            search_exr_by_equipment()
        elif choice == '3':
            for target in targetMuscle:
                print(target.capitalize())
            search_exr_by_target_muscle()
        elif choice == '4':
            search_exr_by_name()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def workout_menu(workout: Workout):

    while True:
        print(f"""\nModifying Workout: {workout.name}
                \n 1. Add Exercise
                \n 2. Remove Exercise
                \n 3. View Exercises
                \n 4. Back to Main Menu""")
        choice = input("Enter your choice: ")

        if choice == '1':
            exercise = search_exercise_menu() 
            if exercise:
                workout.add_exercise_from_workout(exercise)
        elif choice == '2':
            exercise_name = input("Enter the name of the exercise to remove: ") 
            workout.remove_exercise_from_workout(exercise_name)
        elif choice == '3':
            workout.display_workout()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

# Main menu
def main():
    program_manager = ProgramManager()  # Initialize Program Manager
    url = f"{EXERCISEDB_BASE_URL}/status"

    while True:
        print("""\n=== Main Menu ===
            \n 1. Manage Programs
            \n 2. Manage Workouts
            \n 3. Search Exercises
            \n 4. Exit \n""")

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
