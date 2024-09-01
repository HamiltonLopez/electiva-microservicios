from fastapi import APIRouter, Body
from app.models.house_model import House

house_route = APIRouter()


@house_route.post("/")
def create_house(House: House = Body(...)):
    try:
        return house
    except Exception as e:
        return {"error": str(e)}
    
@house_route.get("/{house_id}")
def read_house(house_id: int):
    return {"house_id": house_id}

@house_route.get("/")
def read_houses():
    return {"house_id": "house_id"}

@house_route.put("/{house_id}")
def update_house(house_id: int):
    return {"house_id": house_id}

@house_route.delete("/{house_id}")
def delete_house(house_id: int):
    return {"house_id": house_id}