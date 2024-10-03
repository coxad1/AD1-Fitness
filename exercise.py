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
        return (f"\n{self.name.capitalize()} - Target: {self.target.capitalize()}\n"
                f"Body Part: {self.bodyPart.capitalize()}\n"
                f"Secondary Muscles: {', '.join([muscle.capitalize() for muscle in self.secondaryMuscles])}\n")
