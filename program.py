from typing import Dict, Optional
from .workout import Workout

Days_Of_Week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
class Program:
    def __init__(self, name: str):
        self.name = name
        self.weekly_plan: Dict[str, Optional[Workout]] = {day: None for day in Days_Of_Week}

    def add_workout(self, day: str, workout: Workout):
        if day in self.weekly_plan:
            self.weekly_plan[day] = workout
            print(f"Workout added to {day}.")
        else:
            print("Invalid day. Please choose a day of the week.")

    def remove_workout(self, day: str):
        if day in self.weekly_plan:
            self.weekly_plan[day] = None
            print(f"Workout removed from {day}.")
        else:
            print("Invalid day. Please choose a day of the week.")

    def display_program(self):
        print(f"\nWeekly Workout Plan: {self.name}")
        for day, workout in self.weekly_plan.items():
            if workout:
                print(f"\nDay: {day}")
                print(workout)
            else:
                print(f"\nDay: {day} - No workout scheduled.")

