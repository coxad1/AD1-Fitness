import requests
import os
from dotenv import load_dotenv
from pydantic import ValidationError 
from exercise import Exercise as EX
from programManager import ProgramManager as PM
from workout import Workout as WO

bodyPartTarget = ["back", "cardio", "chest", "lower arms", "lower legs","neck", "shoulders", "upper arms", "upper legs", "waist"]
equipmentUsed = ["assisted", "band", "barbell", "body weight", "bosu ball","cable", "dumbbell", "elliptical machine", "ez barbell","hammer", "kettlebell", "leverage machine", "medicine ball", "olympic barbell", "resistance band", "roller", "rope", "skierg machine", "sled machine", "smith machine", "stability ball","stationary bike", "stepmill machine", "tire", "trap bar","upper body ergometer", "weighted", "wheel roller"]
targetMuscle = ["abductors", "abs", "adductors", "biceps", "calves","cardiovascular system", "delts", "forearms", "glutes","hamstrings", "lats", "levator scapulae", "pectorals","quads", "serratus anterior", "spine", "traps","triceps", "upper back"]

load_dotenv()
exercise_db_api_key = os.getenv('API_KEY')
EXERCISEDB_BASE_URL = "https://exercisedb.p.rapidapi.com"
RAPID_API_HEADERS = {
    'x-rapidapi-key': exercise_db_api_key,
    'x-rapidapi-host': 'exercisedb.p.rapidapi.com'
}

# Function to display the exercises in the response should print via the print statement
def exercise_response(exercises):
    if exercises:
        exercise_list = []
        for id, exercise_data in enumerate(exercises, start=1):
            try:
                exercise = EX(**exercise_data)
                exercise_list.append(exercise)
                print(f"{id}. {exercise.name.capitalize()} - Target: {exercise.target.capitalize()} - Body Part: {exercise.bodyPart.capitalize()}")
            except ValidationError as e:
                print(f"Error: Invalid data for exercise '{exercise_data.get('name', 'Unknown')}' - {e}")
        return exercise_list
    else:
        print("No exercises found. Please try again.")
        return []

# Function pings the API to get the exercises passes the Headers in the resposne alongside the url adds teh response to the workout
def get_exercise_api(url):
    try:
        response = requests.get(url, headers=RAPID_API_HEADERS)
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

# Function extends the search function for exercises and add them to the workout
def select_exercises_to_add(workout: WO):
    while True:
        print("""\nSearch Exercises
                 \n1. Search by Body Part
                 \n2. Search by Equipment
                 \n3. Search by Target Muscle
                 \n4. Search by Name
                 \n5. Done Adding Exercises""")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            url = search_exercise_by_body_part()
        elif choice == '2':
            url = search_exercise_by_equipment()
        elif choice == '3':
            url = search_exercise_by_target_muscle()
        elif choice == '4':
            url = search_exercise_by_name()
        elif choice == '5':
            print("Finished adding exercises.")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        exercises = get_exercise_api(url)
        exercise_list = exercise_response(exercises)

        if not exercise_list:
            continue

        for id, exercise in enumerate(exercise_list, start=1):
            while True:
                add_choice = input(f"Do you want to add '{exercise.name.capitalize()}' to the workout? (y/n): ").strip().lower()
                if add_choice == 'y':
                    workout.add_exercise(exercise)
                    break
                elif add_choice == 'n':
                    print(f"Skipped adding '{exercise.name.capitalize()}'.")
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
        print("Exercise search and addition complete.\n")

# Function serves to search for an exercise by name pinging the API
def search_exercise_by_name():
    while True:
        name = input("\nWhat exercise would you like to search for (or type 'exit' to go back)? ").lower()
        if name == 'exit':
            print("Returning to the previous menu...")
            break
        url = f"{EXERCISEDB_BASE_URL}/exercises/name/{name}"
        return url
# Function serves to search for an exercise by body part pinging the API
def search_exercise_by_body_part():
    print("\nAvailable Body Parts:")
    for body_part in bodyPartTarget:
        print(f"- {body_part.capitalize()}")
    body_part = input("Enter body part: ").lower()
    if body_part not in bodyPartTarget:
        print("Invalid body part. Please choose from the list.")
        url = f"{EXERCISEDB_BASE_URL}/exercises/bodyPart/{body_part}"
        return url
# Function serves to search for an exercise by equipment pinging the API
def search_exercise_by_equipment():
    print("\nAvailable Equipment:")
    for equipment in equipmentUsed:
        print(f"- {equipment.capitalize()}")
    equipment = input("\nEnter equipment: ").lower()
    if equipment not in equipmentUsed:
        print("Invalid equipment. Please choose from the list.")
    url = f"{EXERCISEDB_BASE_URL}/exercises/equipment/{equipment}"
    return url
# Function serves to search for an exercise by target muscle pinging the API
def search_exercise_by_target_muscle():
    print("\nAvailable Target Muscles:")
    for target in targetMuscle:
        print(f"- {target.capitalize()}")
    target = input("Enter target muscle: ").lower()
    if target not in targetMuscle:
        print("Invalid target muscle. Please choose from the list.")
    url = f"{EXERCISEDB_BASE_URL}/exercises/target/{target}"
    return url

def workout_menu(workout: WO):
    while True:
        print(f"\nManaging Workout: {workout.name.capitalize()}")
        print("""\nWorkout Menu:
    1. Add Exercise to Workout
    2. Remove Exercise from Workout
    3. View Exercises in Workout
    4. Return to Program Menu
    """)
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            select_exercises_to_add(workout)  # Call function to add exercises
        elif choice == '2':
            workout.display_exercises()  # Display exercises in the workout
            if not workout.exercises:
                continue
            try:
                index = int(input("Enter the index of the exercise to remove: ")) - 1
                workout.remove_exercise(index)  # Remove the exercise by index
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '3':
            workout.display_exercises()  # Display exercises
        elif choice == '4':
            break  # Exit the workout menu
        else:
            print("Invalid choice. Please try again.")

def main():
    program_manager = PM()
    while True:
        print("""\nMain Menu:
              \n1. Manage Programs\
              \n2. Exit
              \n""")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            program_manager.program_manager_menu()
        elif choice == '2':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()