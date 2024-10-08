from typing import List
from program import Program
from prettytable import PrettyTable
from program import Program
from workout import Workout

class ProgramManager:
    def __init__(self):
        self.programs: List[Program] = []
        self.workouts: List[Workout] = []  
        self.ProgID = len(self.programs) + 1

    # Create a new program and add it to the list
    def create_program(self, program_name: str):
        if not program_name:
            print("Program name cannot be empty.")
            return
        if any(p.name.lower() == program_name.lower() for p in self.programs):
            print(f"Program '{program_name}' already exists.")
            return
        new_program = Program(name=program_name, id=self.ProgID)
        self.programs.append(new_program)
        print(f"\\nProgram '{program_name}' created with ID {self.ProgID}.\\n")
        self.ProgID += 1

    # Display all programs
    def display_programs(self):
        if not self.programs:
            print("No programs available.")
        else:
            table = PrettyTable()
            table.field_names = ["No.", "Program Name", "ID"]
            for idx, program in enumerate(self.programs, start=1):
                table.add_row([idx, program.name, program.id])
            print(table)

        def remove_program(self, program_id: int):
            if 0 <= program_id < len(self.programs):
                removed_program = self.programs.pop(program_id)
                print(f"Program '{removed_program.name}' has been successfully removed.")
            else:
                print("Invalid program ID. Please enter a valid program number.")

    # Create a new workout and add it to the global list of workouts
    def create_workout(self):
        workout_name = input("Enter the name of the new workout: ").strip()
        if workout_name:
            new_workout = Workout(workout_name)
            self.workouts.append(new_workout)
            print(f"Workout '{workout_name}' created successfully and added to the global list of workouts.")
        else:
            print("Workout name cannot be empty.")

    # List all global workouts
    def list_workouts(self):
        if not self.workouts:
            print("No workouts available.")
        else:
            table = PrettyTable()
            table.field_names = ["No.", "Workout Name"]
            for idx, workout in enumerate(self.workouts, start=1):
                table.add_row([idx, workout.name])
            print(table)