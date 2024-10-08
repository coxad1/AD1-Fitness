from typing import List
from workout import Workout
from prettytable import PrettyTable

class Program:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.workouts: List[Workout] = []  
        self.workouts_by_day = {day: [] for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}

    def add_workout(self, workout, day_of_week):
        if day_of_week in self.workouts_by_day:
            self.workouts_by_day[day_of_week].append(workout)
            print(f"Workout '{workout.name}' added to '{day_of_week}' in the program '{self.name}'.")

    def remove_workout(self, day_of_week, workout_index):
        try:
            removed_workout = self.workouts_by_day[day_of_week].pop(workout_index)
            print(f"Workout '{removed_workout.name}' removed from '{day_of_week}' in the program '{self.name}'.")
        except (IndexError, KeyError):
            print("Invalid day or workout index. Please enter a valid number.")
    def display_workouts(self):
        print(f"\n--- {self.name} Program Schedule ---")
        for day, workouts in self.workouts_by_day.items():
            workout_list = ', '.join(workout.name for workout in workouts) if workouts else "Rest"
            print(f"{day}: {workout_list}")

    def list_all_workouts(self):
        print(f"\n--- All Workouts in Program: {self.name} ---")
        for day, workouts in self.workouts_by_day.items():
            for workout in workouts:
                print(f"{day}: {workout.name}")
        if not self.workouts:
            print(f"No workouts in the program '{self.name}'.")
        else:
            table = PrettyTable()
            table.field_names = ["No.", "Workout Name"]
            for idx, workout in enumerate(self.workouts, start=1):
                table.add_row([idx, workout.name])
            print(table)