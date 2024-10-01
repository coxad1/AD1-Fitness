from typing import List
from .exercise import Exercise
from .exercise import search_exercise_menu


class Workout:
    def __init__(self, name: str):
        self.name = name
        self.exercises: List[Exercise] = []

    def add_exercise(self, exercise: Exercise):
        self.exercises.append(exercise)
        print(f"Exercise '{exercise.name}' added to the workout.")

def remove_exercise(self, exercise_name: str):
    for exercise in self.exercises:
        if exercise.name == exercise_name:
            self.exercises.remove(exercise)
            print(f"Exercise '{exercise_name}' removed from the workout.")
            return
        print(f"Exercise '{exercise_name}' not found in the workout.")

    def __str__(self):
        workout_summary = f"Workout: {self.name}\n"
        workout_summary += "\n".join([str(exercise) for exercise in self.exercises])
        return workout_summary

    def workout_menu(workout: Workout):
        while True:
            print(f"\nModifying Workout: {workout.name}")
            print("1. Add Exercise")
            print("2. Remove Exercise")
            print("3. View Exercises")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")
            if choice == '1':
                search_exercise_menu(workout)
            elif choice == '2':
                exercise_name = input("Enter the name of the exercise to remove: ")
                workout.remove_exercise(exercise_name)
                if not workout.exercises:
                    print("No exercises in the workout.")
            elif choice == '3':
                print(workout)
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")