import requests
import os
from dotenv import load_dotenv
from pydantic import ValidationError
from exercise import Exercise
from programManager import ProgramManager

bodyPartTarget = ["back", "cardio", "chest", "lower arms", "lower legs", "neck", "shoulders", "upper arms", "upper legs", "waist"]
equipmentUsed = ["assisted", "band", "barbell", "body weight", "bosu ball", "cable", "dumbbell", "elliptical machine", "ez barbell", "hammer", "kettlebell", "leverage machine", "medicine ball", "olympic barbell", "resistance band", "roller", "rope", "skierg machine", "sled machine", "smith machine", "stability ball", "stationary bike", "stepmill machine", "tire", "trap bar", "upper body ergometer", "weighted", "wheel roller"]
targetMuscle = ["abductors", "abs", "adductors", "biceps", "calves", "cardiovascular system", "delts", "forearms", "glutes", "hamstrings", "lats", "levator scapulae", "pectorals", "quads", "serratus anterior", "spine", "traps", "triceps", "upper back"]

load_dotenv()
exercise_db_api_key = os.getenv('API_KEY')
EXERCISEDB_BASE_URL = "https://exercisedb.p.rapidapi.com"
RAPID_API_HEADERS = {
    'x-rapidapi-key': exercise_db_api_key,
    'x-rapidapi-host': 'exercisedb.p.rapidapi.com'
}

def exercise_response(exercises):
    if exercises:
        for exercise_data in exercises:
            try:
                exercise = Exercise(**exercise_data)
                print(exercise)
            except ValidationError as e: 
                print(f"Error: Invalid data - {e}")
    else:
        print("No exercises found. Please try again.")

def get_exercise_api(url):
    try:
        response = requests.get(url, headers=RAPID_API_HEADERS)
        response.raise_for_status()  # Raise an HTTPError if the response was unsuccessful
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def search_exercise_by_name():
    while True:
        name = input("\nWhat exercise would you like to search for (or type 'exit' to go back)? ").lower()
        if name == 'exit':
            print("Returning to the previous menu...")
            break
        url = f"{EXERCISEDB_BASE_URL}/exercises/name/{name}"
        exercises = get_exercise_api(url)
        exercise_response(exercises)
        break 

def search_exercise_by_body_part():
    body_part = input("What body part would you like to target? ")
    url = f"{EXERCISEDB_BASE_URL}/exercises/bodyPart/{body_part.lower()}"
    exercises = get_exercise_api(url)
    exercise_response(exercises)

def search_exr_by_equipment():
    equipment = input("What equipment would you like to use? ")
    url = f"{EXERCISEDB_BASE_URL}/exercises/equipment/{equipment.lower()}"
    exercises = get_exercise_api(url)
    exercise_response(exercises)

def search_exr_by_target_muscle():
    target = input("What muscle group would you like to target? ")
    url = f"{EXERCISEDB_BASE_URL}/exercises/target/{target.lower()}"
    exercises = get_exercise_api(url)
    exercise_response(exercises)

def search_exercise_menu():
    while True:
        print("""\nSearch Exercises
              \n 1. Search Exercises by Body Part
              \n 2. Search Exercises by Equipment
              \n 3. Search Exercises by Target
              \n 4. Search Exercises by Name
              \n 5. Back to Main Menu \n""")
        
        choice = input("\nEnter your choice: ")

        if choice == '1':
            for body_part in bodyPartTarget: print(f"{body_part}\n")
            search_exercise_by_body_part()
        elif choice == '2':
            for equipment in equipmentUsed: print(equipment)(f"{equipment}\n")
            search_exr_by_equipment()
        elif choice == '3':
            for target in targetMuscle: print(f"{target}\n")
            search_exr_by_target_muscle()
        elif choice == '4':
            search_exercise_by_name()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    program_manager = ProgramManager()  # Initialize Program Manager
    while True:
        print("""\n Main Menu 
            \n 1. Manage Programs
            \n 2. Manage Workouts
            \n 3. Search Exercises
            \n 4. Exit """)

        choice = input("\nEnter your choice: ")

        if choice == '1':
            program_manager.program_manager_menu()  
        elif choice == '2':
            selected_program = program_manager.select_program()
            if selected_program:
                selected_program.program_menu()  
            else:
                print("\nNo programs available. Create a program first.")
        elif choice == '3':
            search_exercise_menu() 
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
