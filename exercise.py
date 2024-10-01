from pydantic import BaseModel, HttpUrl
from typing import List
from main import search_exr_by_body_part, search_exr_by_equipment, search_exr_by_target_muscle, search_exr_by_name

bodyPartTarget = ["back", "cardio", "chest", "lower arms", "lower legs", "neck", "shoulders", "upper arms", "upper legs", "waist"]
equipmentUsed = ["assisted", "band", "barbell", "body weight", "bosu ball", "cable", "dumbbell", "elliptical machine", "ez barbell", "hammer", "kettlebell", "leverage machine", "medicine ball", "olympic barbell", "resistance band", "roller", "rope", "skierg machine", "sled machine", "smith machine", "stability ball", "stationary bike", "stepmill machine", "tire", "trap bar", "upper body ergometer", "weighted", "wheel roller"]
targetMuscle = ["abductors", "abs", "adductors", "biceps", "calves", "cardiovascular system", "delts", "forearms", "glutes", "hamstrings", "lats", "levator scapulae", "pectorals", "quads", "serratus anterior", "spine", "traps", "triceps", "upper back"]

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

def display_exercise(exercise: Exercise):
    print(f"Name: {exercise.name}\n Body Part: {exercise.bodyPart}\n Equipment: {exercise.equipment}\n {exercise.target}\n Secondary Muscles: {', '.join(exercise.secondaryMuscles)}\n GIF URL: {exercise.gifUrl}")
