from typing import List
from exercise import Exercise, search_exercise_menu

class Workout:
    def __init__(self, name: str):
        self.name = name
        self.exercises: List[Exercise] = []

    def add_exercise_from_workout(self, exercise: Exercise):
        self.exercises.append(exercise)
        print(f"Exercise '{exercise.name}' added to the workout.")

    def remove_exercise_from_workout(self, exercise_name: str):
        for exercise in self.exercises:
            if exercise.name == exercise_name: 
                self.exercises.remove(exercise)
                print(f"Exercise '{exercise_name}' removed from the workout.")
                return
        print(f"Exercise '{exercise_name}' not found in the workout.")

    def display_workout(self):
        if not self.exercises:
            print(f"No exercises in workout '{self.name}'.")
        else:
            print(f"Workout: {self.name}")
            for exercise in self.exercises:
                print(f"Exercise: {exercise.name}, Target: {exercise.target}, Equipment: {exercise.equipment}")

    def __str__(self):
        workout_summary = f"Workout: {self.name}\n"
        for exercise in self.exercises:
            workout_summary += f"{exercise}\n"
        return workout_summary

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