from typing import Dict, Optional
from workout import Workout
Days_Of_Week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

class Program:
    def __init__(self, name: str, program_id: int):
        self.name = name
        self.id = program_id
        self.workouts = []

    def create_workout(self):
        workout_name = input("Enter workout name: ")
        new_workout = Workout(workout_name)
        self.workouts.append(new_workout)
        print(f"Workout '{workout_name}' created.")

    def list_workouts(self):
        if not self.workouts:
            print("No workouts available.")
        else:
            for workout in self.workouts:
                print(f"Workout: {workout.name}")

    def program_menu(self):
        while True:
            print(f""""\nProgram Menu for {self.name} 
                \n 1. Create Workout
                \n 2. List Workouts
                \n 3. Modify Workout
                \n 4. Back to Main Menu""")
            choice = input("Enter your choice: ")

            if choice == '1': self.create_workout()
            elif choice == '2': self.list_workouts()
            elif choice == '3':
                if self.workouts:
                    workout_name = input("Enter workout name to modify: ")
                    for workout in self.workouts:
                        if workout.name == workout_name:
                            workout.workout_menu()
                            break
                    else: print("Workout not found.")
                else: print("No workouts available.")
            elif choice == '4':break
            else:print("Invalid choice. Please try again.")

            
