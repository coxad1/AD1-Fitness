from program import Program

class ProgramManager:
    def __init__(self):
        self.programs = []
        self.ProgID = 1

    def create_program(self):
        program_name = input("Enter program name: ")
        self.programs.append(Program(program_name, self.ProgID))
        print(f"Program '{program_name}' created with ID {self.ProgID}.")
        self.ProgID += 1
    
    def list_programs(self):
        for ind_program in self.programs:
            print(f"{ind_program.id}: {ind_program.name}")

    def select_program(self):
        self.list_programs()
        choice = int(input("Enter program ID: "))  
        if 0 < choice <= len(self.programs):
            return self.program_menu(self.programs[choice - 1])
        else:
            print("Invalid ID. Please try again.")

    def manage_program_menu(self):
        while True:
            self.list_programs()
            choice = input("""\n 1. Create Program
                              \n 2. Select Program
                              \n 3. Exit """)
            if choice == '1': self.create_program()
            elif choice == '2': self.select_program()
            elif choice == '3': break