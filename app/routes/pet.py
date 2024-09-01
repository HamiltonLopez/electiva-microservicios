from fastapi import APIRouter, Body
from app.models.pet_model import Pet

pet_route = APIRouter()


@pet_route.post("/")
def create_pet(Pet: Pet = Body(...)):
    try:
        return pet
    except Exception as e:
        return {"error": str(e)}
    
@pet_route.get("/{pet_id}")
def read_pet(pet_id: int):
    return {"pet_id": pet_id}

@pet_route.get("/")
def read_pets():
    return {"pet_id": "pet_id"}

@pet_route.put("/{pet_id}")
def update_pet(pet_id: int):
    return {"pet_id": pet_id}

@pet_route.delete("/{pet_id}")
def delete_pet(pet_id: int):
    return {"pet_id": pet_id}
