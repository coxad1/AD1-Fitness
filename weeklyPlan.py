from typing import Dict, Optional
from .workout import Workout

class Week:
    Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def __init__(self):
        self.weekly_plan: Dict[str, Optional[Workout]] = {day: None for day in self.Days}

    def add_workout(self, day: str, workout: Workout):
        if day in self.Days:
            self.weekly_plan[day] = workout
            print(f"Workout added to {day}.")
        else:
            print("Invalid day. Please choose a day of the week.")  

    def remove_workout(self, day: str):
        if day in self.Days:
            self.weekly_plan[day] = None
            print(f"Workout removed from {day}.")
        else:
            print("Invalid day. Please choose a day of the week.")

    
    def display_weekly_plan(self):
        for day, workout in self.weekly_plan:
            if workout:
                print(f"\n{day}:")
                print(workout)
            else:
                print(f"{day}: Rest day")