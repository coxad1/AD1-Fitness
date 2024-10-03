from pydantic import BaseModel
from typing import List
from exercise import Exercise
from prettytable import PrettyTable

class Workout(BaseModel):
    name: str
    exercises: List[Exercise] = []

    def add_exercise(self, exercise: Exercise):
        if any(ex.name.lower() == exercise.name.lower() for ex in self.exercises):
            print(f"Exercise '{exercise.name}' is already in the workout.")
            return
        self.exercises.append(exercise)
        print(f"Exercise '{exercise.name}' added to the workout.")

    def remove_exercise(self, index: int):
        if 0 <= index < len(self.exercises):
            removed = self.exercises.pop(index)
            print(f"Exercise '{removed.name}' removed from the workout.")
        else:
            print("Invalid exercise index.")

    def display_exercises(self):
        if not self.exercises:
            print("No exercises in this workout.")
            return
        table = PrettyTable()
        table.field_names = ["Index", "Name", "Target Muscle", "Body Part"]
        for idx, exercise in enumerate(self.exercises, start=1):
            table.add_row([idx, exercise.name.capitalize(), exercise.target.capitalize(), exercise.bodyPart.capitalize()], divider=True)
        print(table)

    def __str__(self):
        return f"Workout: {self.name.capitalize()} with {len(self.exercises)} exercises."
