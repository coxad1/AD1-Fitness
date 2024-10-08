import requests
import os
from dotenv import load_dotenv
from programManager import ProgramManager as PM
from prettytable import PrettyTable
from pydantic import ValidationError
from exercise import Exercise

# Load environment variables for API keys
load_dotenv()
EXERCISEDB_API_KEY = os.getenv('API_KEY')
EXERCISEDB_BASE_URL = "https://exercisedb.p.rapidapi.com"
RAPID_API_HEADERS = {
    'x-rapidapi-key': EXERCISEDB_API_KEY,
    'x-rapidapi-host': 'exercisedb.p.rapidapi.com'
}

bodyPartTarget = ["back", "cardio", "chest", "lower arms", "lower legs","neck", "shoulders", "upper arms", "upper legs", "waist"]
equipmentUsed = ["assisted", "band", "barbell", "body weight", "bosu ball","cable", "dumbbell", "elliptical machine", "ez barbell","hammer", "kettlebell", "leverage machine", "medicine ball", "olympic barbell", "resistance band", "roller", "rope", "skierg machine", "sled machine", "smith machine", "stability ball","stationary bike", "stepmill machine", "tire", "trap bar","upper body ergometer", "weighted", "wheel roller"]
targetMuscle = ["abductors", "abs", "adductors", "biceps", "calves","cardiovascular system", "delts", "forearms", "glutes","hamstrings", "lats", "levator scapulae", "pectorals","quads", "serratus anterior", "spine", "traps","triceps", "upper back"]

# Function to fetch the response and status of the API
def fetch_and_display_exercises(url):
    try:
        response = requests.get(url, headers=RAPID_API_HEADERS)
        response.raise_for_status()
        exercises_data = response.json() 
        exercises = [Exercise(**exercise) for exercise in exercises_data]
        display_exercises_table(exercises)
        return exercises
    except ValidationError as e:
        print(f"Error fetching exercises: {e}")
        return []
    
# Function to search for exercises based on body part, equipment, or target muscle
def search_exercises_menu(pm):
    while True:
        print("""\n--- Exercise Search Menu ---
        \n1. Search by Body Part
        \n2. Search by Equipment
        \n3. Search by Target Muscle
        \n4. Search by Exercise Name
        \n5. Return to Main Menu""")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            exercises = search_by_body_part()
        elif choice == "2":
            exercises = search_by_equipment()
        elif choice == "3":
            exercises = search_by_target()
        elif choice == "4":
            exercises = search_by_name()
        elif choice == "5":
            break
        else:
            print("Invalid choice, please enter a number between 1 and 4.")
            continue
        if exercises:
            add_exercise_to_workout(pm, exercises)

# Function to add an exercise to a workout
def add_exercise_to_workout(pm, exercises):
    while True:
        add_exercise_choice = input("Would you like to add an exercise to a workout? (y/n): ").strip().lower()
        if add_exercise_choice == "y":
            pm.list_workouts()
            try:
                workout_index = int(input("Enter the number of the workout to add an exercise to (or '0' to cancel): ")) - 1
                if workout_index == -1:
                    print("Returning to exercise search menu.")
                    break
                elif 0 <= workout_index < len(pm.workouts):
                    selected_workout = pm.workouts[workout_index]
                    print(f"Selected workout: {selected_workout.name}")

                    exercise_index = int(input("Enter the number of the exercise to add from the search results: ")) - 1
                    if 0 <= exercise_index < len(exercises):
                        selected_exercise = exercises[exercise_index]
                        selected_workout.add_exercise(selected_exercise)  
                        print(f"Exercise '{selected_exercise.name}' added to workout '{selected_workout.name}'.")
                    else:
                        print("Invalid exercise number. Please enter a valid exercise index.")
                else:
                    print("Invalid workout number. Please enter a valid workout index.")
            except ValueError:
                print("Please enter a valid number.")
        elif add_exercise_choice == "n":
            print("Returning to exercise search menu.")
            break
        else:
            print("Invalid choice. Please enter 'y' to add an exercise or 'n' to return to the search menu.")

# Function to add a workout to a program
def add_workout_to_program(program, pm):
    if not pm.workouts:
        print("No workouts available to add. Please create a workout first.")
        return

    print("\n--- Available Workouts ---")
    pm.list_workouts()  # Display the list of existing workouts

    try:
        workout_index = int(input("Enter the number of the workout to add to the program (or '0' to cancel): ")) - 1
        if workout_index == -1:
            print("Returning to the program modification menu.")
        elif 0 <= workout_index < len(pm.workouts):
            selected_workout = pm.workouts[workout_index]
            program.add_workout(selected_workout)
            print(f"Workout '{selected_workout.name}' has been added to the program '{program.name}'.")
        else:
            print("Invalid workout number. Please enter a valid workout index.")
    except ValueError:
        print("Please enter a valid number.")

# Functions to search for exercises based on the name, attempts a match 
def search_by_name():
    while True:
        name = input("\nWhat exercise would you like to search for? ").strip().lower()
        if name:
            url = f"{EXERCISEDB_BASE_URL}/exercises/name/{name}"
            return fetch_and_display_exercises(url)
        else:
            print("Please enter a valid exercise name.")

# Functions to search for exercises based on the target muscle, also parses the user input initially to make sure its in the list of target muscles
def search_by_target():
    for index, muscle in enumerate(targetMuscle, start=1):
        print(f"{index}. {muscle.capitalize()}")
    while True:
        target_muscle = input("Enter the target muscle to search for exercises (e.g., biceps, quadriceps): ").strip().lower()
        if target_muscle:  # Ensure the user entered a value
            url = f"{EXERCISEDB_BASE_URL}/exercises/target/{target_muscle}"
            return fetch_and_display_exercises(url)
        else:
            print("Please enter a valid target muscle.")

# Functions to search for exercises based on the equipment used, also parses the user input initially to make sure its in the list of equipment used
def search_by_equipment():
    for index, equipment in enumerate(equipmentUsed, start=1):
        print(f"{index}. {equipment.capitalize()}")
    while True:
        equipment = input("Enter the equipment to search for exercises (e.g., dumbbell, barbell): ").strip().lower()
        if equipment:  # Ensure the user entered a value
            url = f"{EXERCISEDB_BASE_URL}/exercises/equipment/{equipment}"
            return fetch_and_display_exercises(url)
        else:
            print("Please enter a valid equipment type.")

# Functions to search for exercises based on the body part, also parses the user input initially to make sure its in the list of body parts targeted
def search_by_body_part():
    for index, body_part in enumerate(bodyPartTarget, start=1):
        print(f"{index}. {body_part.capitalize()}")
    while True:
        body_part = input("Enter the body part to search for exercises (e.g., chest, legs, arms): ").strip().lower()
        if body_part:  #
            url = f"{EXERCISEDB_BASE_URL}/exercises/bodyPart/{body_part}"
            return fetch_and_display_exercises(url)
        else:
            print("Please enter a valid body part.")

# Function to display the exercises in a table format
def display_exercises_table(exercises):
    if exercises:
        table = PrettyTable()
        table.field_names = ["No.", "Exercise Name", "Body Part", "Equipment", "Target Muscle"]
        
        for id, exercise in enumerate(exercises, start=1):
            table.add_row([id, exercise.name, exercise.bodyPart, exercise.equipment, exercise.target])

        print(table)
    else:
        print("No exercises found.")

# Function to display the primary menu for the program manager
def primary_menu(pm):
    while True:
        print("""\n--- Welcome to Your Personal Training Program Builder ---
                 \n1. Create a New Training Program
                 \n2. Create a New Workout
                 \n3. View All Programs
                 \n4. View All Workouts
                 \n5. Add Workouts to a Program
                 \n6. Modify a Program (View or Remove Workouts)
                 \n7. Modify a Workout (View or Remove Exercises)
                 \n8. Search for Exercises
                 \n9. Export a Program
                 \n10. Remove a Program
                 \n11. Exit the Application""")

        choice = input("Enter your choice (1-11): ").strip()
        if choice == "1":
            program_name = input("Enter the name of the new program: ").strip()
            pm.create_program(program_name)
        elif choice == "2":
            pm.create_workout()  
        elif choice == "3":
            pm.display_programs()
        elif choice == "4":
            pm.list_workouts()
        elif choice == "5":
            pm.add_workout_to_program()
        elif choice == "6":
            modify_program_menu(pm)
        elif choice == "7":
            modify_workout_menu(pm)
        elif choice == "8":
            search_exercises_menu(pm)
        elif choice == "9":
            export_program_menu(pm)
        elif choice == "10":
            pm.display_programs()
            program_id = int(input("Enter the ID of the program to remove: ")) - 1
            pm.remove_program(program_id)
        elif choice == "11":
            print("Thank you for using the Personal Training Program Builder. Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 11.")

# Function to modify a program by viewing or removing workouts
def modify_program_menu(pm):
    print("\n--- Program Modification Menu ---")
    pm.display_programs()
    try:
        program_index = int(input("Enter the number of the program you want to modify (or '0' to go back): ")) - 1
        if program_index == -1:
            return
        elif 0 <= program_index < len(pm.programs):
            selected_program = pm.programs[program_index]
            while True:
                print(f"\nManaging Program: {selected_program.name}")
                print("1. View All Workouts in this Program")
                print("2. Add an Existing Workout to this Program")
                print("3. Remove a Workout from this Program")
                print("4. Return to the Main Menu")
                choice = input("Choose an option (1-4): ").strip()
                if choice == "1":
                    selected_program.display_workouts()
                elif choice == "2":
                    add_workout_to_program(selected_program, pm)  # Pass both the program and program manager
                elif choice == "3":
                    workout_index = int(input("Enter the number of the workout to remove: ")) - 1
                    selected_program.remove_workout(workout_index)
                elif choice == "4":
                    break
                else:
                    print("Invalid choice, please enter a number between 1 and 4.")
        else:
            print("Invalid program selection. Please enter a valid number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to modify a workout by viewing or removing exercises 
def modify_workout_menu(pm):
    print("\n--- Workout Modification Menu ---")
    pm.list_workouts()
    try:
        workout_index = int(input("Enter the number of the workout you want to modify (or '0' to go back): ")) - 1
        if workout_index == -1:
            return
        elif 0 <= workout_index < len(pm.workouts):
            selected_workout = pm.workouts[workout_index]
            while True:
                print(f"""\nManaging Workout: {selected_workout.name}
                \n1. View All Exercises in this Workout
                \n2. Add an Exercise to this Workout
                \n3. Remove an Exercise from this Workout
                \n4. Return to the Main Menu""")
                choice = input("Choose an option (1-4): ").strip()
                if choice == "1":
                    selected_workout.display_exercises()
                elif choice == "2":
                    search_exercises_menu(pm)
                elif choice == "3":
                    selected_workout.remove_exercise()
                elif choice == "4":
                    break
                else:
                    print("Invalid choice, please enter a number between 1 and 4.")
        else:
            print("Invalid workout selection. Please enter a valid number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to export a program to a text file
def export_program_menu(pm):
    print("\n--- Export Program Menu ---")
    pm.display_programs()
    try:
        program_index = int(input("Enter the number of the program to export (or '0' to go back): ")) - 1
        if program_index == -1:
            return
        elif 0 <= program_index < len(pm.programs):
            selected_program = pm.programs[program_index]
            export_program(selected_program)
        else:
            print("Invalid program selection. Please enter a valid number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to export a program to a text file
def export_program(program):
    file_name = f"{program.name}_Program.txt"
    with open(file_name, 'w') as file:
        file.write(f"--- {program.name} Program ---\n\n")

        for workout in program.workouts:
            file.write(f"Workout: {workout.name}\n")
            file.write("Exercises:\n")

            # Create a PrettyTable for the exercises
            table = PrettyTable()
            table.field_names = ["Exercise Name", "Target Muscle", "Equipment", "Secondary Muscles", "GIF URL"]

            for exercise in workout.exercises:
                secondary_muscles = ', '.join(exercise.secondaryMuscles) if exercise.secondaryMuscles else "N/A"
                table.add_row([
                    exercise.name.capitalize(),
                    exercise.target.capitalize(),
                    exercise.equipment.capitalize(),
                    secondary_muscles,
                    exercise.gifUrl
                ])
                for set_number in range(1,4): 
                    table.add_row([
                        f"  Set {set_number}",
                        f"Reps: [   ]",
                        f"Weight: [   ]",
                        "",  # Empty cells for the secondary muscles and GIF URL columns
                        ""
                    ])
            # Write the PrettyTable to the file
            file.write(table.get_string())
            file.write("\n\n")

    print(f"Program successfully exported to {file_name}.")

# Main function to run the program entrance point
def main():
    pm = PM()  
    primary_menu(pm)  

if __name__ == "__main__":
    main()