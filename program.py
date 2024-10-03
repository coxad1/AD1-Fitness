from pydantic import BaseModel
from typing import List
from workout import Workout
from prettytable import PrettyTable

class Program(BaseModel):
    name: str
    id: int
    workouts: List[Workout] = []

    def add_workout(self, workout_name: str, program_manager):
        if any(w.name.lower() == workout_name.lower() for w in self.workouts):
            print(f"Workout '{workout_name}' already exists in the program.")
            return
        new_workout = Workout(name=workout_name)
        self.workouts.append(new_workout)
        print(f"Workout '{workout_name}' added to program '{self.name}'.")

    def remove_workout(self, index: int):
        try:
            if 0 <= index < len(self.workouts):
                removed = self.workouts.pop(index)
                print(f"Workout '{removed.name}' removed from the program.")
            else:
                print("Invalid workout index.")
        except ValueError:
            print("Please enter a valid index number.")


    def display_workouts(self):
        if not self.workouts:
            print("No workouts in this program.")
            return
        table = PrettyTable()
        table.field_names = ["Index", "Workout Name", "Number of Exercises"]
        for i, workout in enumerate(self.workouts, start=1):
            table.add_row([i, workout.name.capitalize(), len(workout.exercises)])
        print(table)

    def display_program_menu(self):
        print(f"\nManaging Program: {self.name}")
        print("Program Menu:\n1. Add Workout\n2. Remove Workout\n3. View Workouts\n4. Exit")

    def program_menu(self, program_manager):
        while True:
            self.display_program_menu()
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                workout_name = input("Enter the workout name: ")
                self.add_workout(workout_name, program_manager)
            elif choice == '2':
                self.display_workouts()
                try:
                    index = int(input("Enter workout index to remove: ")) - 1
                    self.remove_workout(index)
                except ValueError:
                    print("Invalid input.")
            elif choice == '3':
                self.display_workouts()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Try again.")
