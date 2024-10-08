from pydantic import BaseModel, HttpUrl
from typing import List
# Base model class to take in the JSON response and format it into a class object
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
