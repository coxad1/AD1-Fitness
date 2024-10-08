from typing import List
from workout import Workout
from prettytable import PrettyTable

class Program:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id  # Add the id attribute to the constructor
        self.workouts: List[Workout] = []  # Initialize an empty list of workouts

    # Add a workout to the program using a workout object from the global list
    def add_workout(self, workout: Workout):
        if any(w.name.lower() == workout.name.lower() for w in self.workouts):
            print(f"Workout '{workout.name}' already exists in the program.")
            return
        self.workouts.append(workout)
        print(f"Workout '{workout.name}' added to program '{self.name}'.")
        
    # Display all workouts within the program
    def display_workouts(self):
        if not self.workouts:
            print(f"No workouts in the program '{self.name}'.")
        else:
            table = PrettyTable()
            table.field_names = ["No.", "Workout Name"]
            for idx, workout in enumerate(self.workouts, start=1):
                table.add_row([idx, workout.name])
            print(table)