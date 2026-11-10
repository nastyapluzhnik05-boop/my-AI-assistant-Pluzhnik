import logging
from pydantic import BaseModel, Field

class StudentInfo(BaseModel):
    name: str
    group: int
    score: int

