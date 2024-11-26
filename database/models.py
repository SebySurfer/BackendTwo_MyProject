from pydantic import BaseModel

class User(BaseModel):
    firstName: str
    lastName: str
    is_Registered: bool = False