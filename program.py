from typing import List
from workout import Workout
from prettytable import PrettyTable

class Program:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.workouts: List[Workout] = []  # Initialize an empty list of workouts

    # Add a workout to the program if it doesn't already exist
    def add_workout(self, workout_name: str):
        if any(w.name.lower() == workout_name.lower() for w in self.workouts):
            print(f"Workout '{workout_name}' already exists in the program.")
            return
        new_workout = Workout(name=workout_name)
        self.workouts.append(new_workout)
        print(f"Workout '{workout_name}' added to program '{self.name}'.")

    # Remove a workout from the program by index
    def remove_workout(self, index: int):
        if 0 <= index < len(self.workouts):
            removed = self.workouts.pop(index)
            print(f"Workout '{removed.name}' removed from the program.")
        else:
            print("Invalid workout index.")

    # Display all workouts in the program with their exercises count
    def display_workouts(self):
        if not self.workouts:
            print("No workouts in this program.")
            return
        table = PrettyTable()
        table.field_names = ["Index", "Workout Name", "Number of Exercises"]
        for i, workout in enumerate(self.workouts, start=1):
            table.add_row([i, workout.name.capitalize(), len(workout.exercises)])
        print(table)
