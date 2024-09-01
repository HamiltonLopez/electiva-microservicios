from pydantic import BaseModel

class House(BaseModel):
    id: int
    username: str
    type: str
    age: int 
    color: str


