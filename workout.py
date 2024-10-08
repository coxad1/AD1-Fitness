from typing import List
from exercise import Exercise
from prettytable import PrettyTable

class Workout:
    def __init__(self, name: str):
        self.name = name
        self.exercises: List[Exercise] = []

    def add_exercise(self, exercise: Exercise):
        self.exercises.append(exercise)
        print(f"Exercise '{exercise.name}' added to workout '{self.name}'.")

    def remove_exercise(self):
        self.display_exercises()
        try:
            index = int(input("Enter the number of the exercise to remove: ")) - 1
            if 0 <= index < len(self.exercises):
                removed = self.exercises.pop(index)
                print(f"Exercise '{removed.name}' removed from workout '{self.name}'.")
            else:
                print("Invalid exercise number.")
        except ValueError:
            print("Please enter a valid number.")

    def display_exercises(self):
        if not self.exercises:
            print(f"No exercises in the workout '{self.name}'.")
        else:
            table = PrettyTable()
            table.field_names = ["No.", "Exercise Name", "Target Muscle", "Equipment"]
            for idx, exercise in enumerate(self.exercises, start=1):
                table.add_row([idx, exercise.name, exercise.target, exercise.equipment])
            print(table)