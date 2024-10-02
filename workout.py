from typing import List
from exercise import Exercise
from prettytable import PrettyTable

class Workout:
    def __init__(self, name: str):
        self.name = name
        self.exercises: List[Exercise] = []

    def insert_exercise_into_workout(self, exercise: Exercise):
        self.exercises.append(exercise)
        print(f"Exercise '{exercise.name}' added to the workout.")

    def erase_exercise_from_workout(self, exercise_name: str):
        for exercise in self.exercises:
            if exercise.name == exercise_name: 
                self.exercises.remove(exercise)
                print(f"Exercise '{exercise_name}' removed from the workout.")
                return
        print(f"Exercise '{exercise_name}' not found in the workout.")

    def display_exercises(self):
            if self.exercises:
                table = PrettyTable()
                table.field_names = ["Exercise"]
                for exercise in self.exercises:
                    table.add_row([exercise])
                print(table)
            else:
                print("No exercises.")

    def __str__(self):
        workout_summary = f"Workout: {self.name}\n"
        for exercise in self.exercises:
            workout_summary += f"{exercise}\n"
        return workout_summary
    
    def workout_menu(self):
        while True:
            choice = input("""\n1. Add Exercise to Workout
                           \n2. Erase Exercise from Workout
                           \n3. View Exercises in Workout
                           \n4. Exit: """)
            if choice == '1': self.insert_exercise_into_workout()
            elif choice == '2': self.erase_exercise_from_workout()
            elif choice == '3': self.display_exercises()
            elif choice == '4': break

    