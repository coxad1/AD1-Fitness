from typing import List
from exercise import Exercise

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
    