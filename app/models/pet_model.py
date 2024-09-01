from pydantic import BaseModel

class Pet(BaseModel):
    id: int
    username: str
    type: str
    age: int
    color: str

