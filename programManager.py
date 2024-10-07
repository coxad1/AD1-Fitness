from typing import List, Optional
from program import Program
from prettytable import PrettyTable

class ProgramManager:
    def __init__(self):
        self.programs: List[Program] = []
        self.ProgID = 1  # Unique identifier for programs

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
        print(f"\nProgram '{program_name}' created with ID {self.ProgID}.\n")
        self.ProgID += 1
    
    # List all programs in a table
    def list_programs(self):
        if not self.programs:
            print("No programs available.")
            return
        table = PrettyTable()
        table.field_names = ["Program ID", "Program Name"]
        for program in self.programs:
            table.add_row([program.id, program.name.capitalize()])
        print(table)

    # Select a program by its ID
    def select_program(self) -> Optional[Program]:
        self.list_programs()
        if not self.programs:
            return None
        try:
            choice = int(input("Enter Program ID to select: ").strip())
            for program in self.programs:
                if program.id == choice:
                    print(f"\nSelected Program: {program.name.capitalize()}\n")
                    return program
            print("Invalid Program ID.")
            return None
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None
        
    # Remove a program by its ID
    def remove_program(self):
        self.list_programs()
        if not self.programs:
            return
        try:
            choice = int(input("Enter Program ID to remove: ").strip())
            for idx, program in enumerate(self.programs):
                if program.id == choice:
                    removed = self.programs.pop(idx)
                    print(f"Program '{removed.name}' removed successfully.")
                    return
            print("Program ID not found.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Add a workout to a selected program
    def add_workout_to_program(self):
        selected_program = self.select_program()
        if selected_program:
            workout_name = input("Enter workout name: ").strip()
            if workout_name:
                selected_program.add_workout(workout_name)
            else:
                print("Workout name cannot be empty.")
