from pydantic import BaseModel

class Phone(BaseModel):
    id: int
    color: str
    storage: str
    brand: str
    model: str

    

