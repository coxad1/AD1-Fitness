from pydantic import BaseModel, HttpUrl
from typing import List
from .main import search_exr_by_body_part, search_exr_by_equipment, search_exr_by_target_muscle, search_exr_by_name

bodyPartTarget = ["back", "cardio", "chest", "lower arms", "lower legs", "neck", "shoulders", "upper arms", "upper legs", "waist"]
equipmentUsed = ["assisted", "band", "barbell", "body weight", "bosu ball", "cable", "dumbbell", "elliptical machine", "ez barbell", "hammer", "kettlebell", "leverage machine", "medicine ball", "olympic barbell", "resistance band", "roller", "rope", "skierg machine", "sled machine", "smith machine", "stability ball", "stationary bike", "stepmill machine", "tire", "trap bar", "upper body ergometer", "weighted", "wheel roller"]
targetMuscle = ["abductors", "abs", "adductors", "biceps", "calves", "cardiovascular system", "delts", "forearms", "glutes", "hamstrings", "lats", "levator scapulae", "pectorals", "quads", "serratus anterior", "spine", "traps", "triceps", "upper back"]

# Base class for an Exercise
class Exercise(BaseModel):
    bodyPart: str
    equipment: str
    gifUrl: HttpUrl
    id: str
    name: str
    target: str
    secondaryMuscles: List[str]
    instructions: List[str]

    def __str__(self):
        return f"{self.name} targeting {self.target}"

def search_exercise_menu(exercise: Exercise):
        while True:
            print(f"\nSearch Exercises")
            print("1. Search Exercises by Body Part")
            print("2. Search Exercises by Equipment")
            print("3. Search Exercises by Target")
            print("4. Search Exercises by Name")
            print("5. Back to Main Menu")
        
            choice = input("Enter your choice: ")
            if choice == '1':
                search_exr_by_body_part(exercise)
            elif choice == '2':
                search_exr_by_equipment(exercise)
            elif choice == '3':
                search_exr_by_target_muscle(exercise)
            elif choice == '4':
                search_exr_by_name(exercise)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")