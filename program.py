from prettytable import PrettyTable
from workout import Workout

class Program:
    def __init__(self, name, program_id):
        self.name, self.id, self.weekly_plan = name, program_id, {day: None for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}

    def add_workout(self, day):
        workout_name = input("Enter workout name: ")
        self.weekly_plan[day] = Workout(workout_name)
        print(f"Workout '{workout_name}' added to {day}.")
        self.weekly_plan[day].workout_menu()

    def display_weekly_program(self):
        table = PrettyTable()
        table.field_names = ["Day", "Workout"]
        for day, workout in self.weekly_plan.items():
            if workout:
                table.add_row([day, workout.name])
            else:
                table.add_row([day, "No workout scheduled"])
        print(table)

    def program_menu(self):
        while True:
            choice = input(""""\n1. Add Workout
                           \n2. View Program
                           \n3. Back
                           \nChoose: """)
            if choice == '1':
                self.add_workout(input("Enter day: "))
            elif choice == '2':
                self.display_weekly_program()
            elif choice == '3':
                break