import requests
import os
from dotenv import load_dotenv
from pydantic import ValidationError 
from exercise import Exercise as EX
from programManager import ProgramManager as PM
from workout import Workout as WO

# Load environment variables and API keys
load_dotenv()
exercise_db_api_key = os.getenv('API_KEY')
EXERCISEDB_BASE_URL = "https://exercisedb.p.rapidapi.com"
RAPID_API_HEADERS = {
    'x-rapidapi-key': exercise_db_api_key,
    'x-rapidapi-host': 'exercisedb.p.rapidapi.com'
}

bodyPartTarget = ["back", "cardio", "chest", "lower arms", "lower legs","neck", "shoulders", "upper arms", "upper legs", "waist"]
equipmentUsed = ["assisted", "band", "barbell", "body weight", "bosu ball","cable", "dumbbell", "elliptical machine", "ez barbell","hammer", "kettlebell", "leverage machine", "medicine ball", "olympic barbell", "resistance band", "roller", "rope", "skierg machine", "sled machine", "smith machine", "stability ball","stationary bike", "stepmill machine", "tire", "trap bar","upper body ergometer", "weighted", "wheel roller"]
targetMuscle = ["abductors", "abs", "adductors", "biceps", "calves","cardiovascular system", "delts", "forearms", "glutes","hamstrings", "lats", "levator scapulae", "pectorals","quads", "serratus anterior", "spine", "traps","triceps", "upper back"]

# API exercise response function
def exercise_response(exercises):
    if exercises:
        for idx, exercise in enumerate(exercises, start=1):
            print(f"{idx}. {exercise['name']} - {exercise['target']}")
    else:
        print("No exercises found.")

# Fetch exercises based on a search criterion
def search_exercises_by_target(target):
    url = f"{EXERCISEDB_BASE_URL}/exercises/target/{target}"
    response = requests.get(url, headers=RAPID_API_HEADERS)
    exercises = response.json()
    exercise_response(exercises)
    return exercises

# Function for searching exercises by body part
def search_exercises_by_bodypart():
    print("Search by body part:")
    for idx, bodypart in enumerate(bodyPartTarget, start=1):
        print(f"{idx}. {bodypart.capitalize()}")

    try:
        bodypart_choice = int(input("Select a body part: ")) - 1
        if 0 <= bodypart_choice < len(bodyPartTarget):
            bodypart = bodyPartTarget[bodypart_choice]
            url = f"{EXERCISEDB_BASE_URL}/exercises/bodyPart/{bodypart}"
            response = requests.get(url, headers=RAPID_API_HEADERS)
            exercises = response.json()
            exercise_response(exercises)
            return exercises
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function for searching exercises by equipment
def search_exercises_by_equipment():
    print("Search by equipment:")
    for idx, equipment in enumerate(equipmentUsed, start=1):
        print(f"{idx}. {equipment.capitalize()}")

    try:
        equipment_choice = int(input("Select equipment: ")) - 1
        if 0 <= equipment_choice < len(equipmentUsed):
            equipment = equipmentUsed[equipment_choice]
            url = f"{EXERCISEDB_BASE_URL}/exercises/equipment/{equipment}"
            response = requests.get(url, headers=RAPID_API_HEADERS)
            exercises = response.json()
            exercise_response(exercises)
            return exercises
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to search and optionally add exercises to a workout
def search_exercises_menu(workout=None):
    print("\n--- Exercise Search Menu ---")
    print("1. Search by Target Muscle")
    print("2. Search by Body Part")
    print("3. Search by Equipment")
    print("4. Return to Program Manager Menu")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        target = input("Enter target muscle: ").strip().lower()
        exercises = search_exercises_by_target(target)
    elif choice == "2":
        exercises = search_exercises_by_bodypart()
    elif choice == "3":
        exercises = search_exercises_by_equipment()
    elif choice == "4":
        return
    else:
        print("Invalid choice.")

    if workout:
        add_exercise_choice = input("Would you like to add an exercise to the workout? (y/n): ").strip().lower()
        if add_exercise_choice == "y":
            selected_idx = int(input("Select an exercise to add: ")) - 1
            try:
                selected_exercise = EX(**exercises[selected_idx])
                workout.add_exercise(selected_exercise)
            except (ValidationError, IndexError):
                print("Error adding exercise to the workout.")
        else:
            print("Returning to menu...")

# Function for managing workouts
def workout_menu(pm):
    selected_workout = pm.select_workout_in_program()
    if not selected_workout:
        return

    while True:
        print("\n--- Manage Workout ---")
        print("1. View Exercises")
        print("2. Search and Add Exercises")
        print("3. Return to Program Manager Menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            selected_workout.display_exercises()
        elif choice == "2":
            search_exercises_menu(selected_workout)
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")

# Program Manager Menu (Main Menu)
def program_manager_menu(pm):
    while True:
        print("\n--- Program Manager Menu ---")
        print("1. Search Programs")
        print("2. Search Available Exercises")
        print("3. Create New Program")
        print("4. Add Workout to Program")
        print("5. Add Exercises to a Workout")
        print("6. Remove Program")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            pm.list_programs()
        elif choice == "2":
            search_exercises_menu()
        elif choice == "3":
            program_name = input("Enter new program name: ").strip()
            pm.create_program(program_name)
        elif choice == "4":
            pm.add_workout_to_program()
        elif choice == "5":
            workout_menu(pm)
        elif choice == "6":
            pm.remove_program()
        elif choice == "7":
            print("Exiting application.")
            break
        else:
            print("Invalid choice, please try again.")

# Main function to initialize and run the program
def main():
    pm = PM()  # Initialize ProgramManager
    program_manager_menu(pm)  # Start Program Manager Menu

# Entry point for the program
if __name__ == "__main__":
    main()