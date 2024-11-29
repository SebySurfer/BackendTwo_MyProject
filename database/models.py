from pydantic import BaseModel
from typing import List

class User(BaseModel):
    firstName: str
    lastName: str
    gender: str
    atGender: str
    phoneNumber: str
    instagram: str
    questions: List[str] = []
    is_Registered: bool = False

class QuestionsUpdate(BaseModel):
    questions: List[str]