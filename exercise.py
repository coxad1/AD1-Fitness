from pydantic import BaseModel, HttpUrl
from typing import List

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
