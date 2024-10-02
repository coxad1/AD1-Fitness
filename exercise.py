from pydantic import BaseModel, HttpUrl
from typing import List

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
