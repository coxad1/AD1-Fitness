from typing import List
from .exercise import Exercise


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
