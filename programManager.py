from program import Program
from prettytable import PrettyTable

class ProgramManager:
    def __init__(self):
        self.programs = []
        self.ProgID = 1

    def create_program(self):
        program_name = input("\nEnter program name:")
        self.programs.append(Program(program_name, self.ProgID))
        print(f"\nProgram '{program_name}' created with ID {self.ProgID}.\n")
        self.ProgID += 1
    
    def list_programs(self):
            table = PrettyTable()
            table.field_names = ["Program ID", "Program Name"]
            for program in self.programs:
                table.add_row([program.id, program.name])
            print(table)

    def select_program(self):
        self.list_programs()
        choice = int(input("Enter program ID: \n"))  
        if 0 < choice <= len(self.programs):
            return self.programs[choice - 1]
        else:
            print("Invalid ID. Please try again.")

    def program_manager_menu(self):
        while True:
            choice = input("""\n 1. Create Program
                              \n 2. Select Program by ID
                              \n 3. Exit \n """)
            
            if choice == '1': self.create_program()
            elif choice == '2': self.select_program()
            elif choice == '3': break