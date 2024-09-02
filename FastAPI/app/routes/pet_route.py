from fastapi import APIRouter, Body
from models.pet_model import Pet

pet_route = APIRouter()


@pet_route.post("/")
def create_pet(Pet: Pet = Body(...)):
    PetModel.create(name=Pet.name, breed=Pet.breed, age=Pet.age, color=Pet.color)
    return Pet
    
@pet_route.get("/{pet_id}")
def read_pet(pet_id: int):
    try:
        pet = PetModel.get_by_id(pet_id)
        return {"id": pet.id, "name": pet.name, "breed": pet.breed, "age": pet.age, "color": pet.color}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Pet not found")

@pet_route.get("/")
def read_pets():
    pets = list(PetModel.select())
    return pets

@pet_route.put("/{pet_id}")
def update_pet(pet_id: int):
        
            pet = PetModel.get_by_id(pet_id)
            pet.update(**pet_data)
            return pet

@pet_route.delete("/{pet_id}")
def delete_pet(pet_id: int):
    try:
        pet = PetModel.delete(PetModel.id == pet_id)
        return {"message": "Pet deleted"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Pet not found")
