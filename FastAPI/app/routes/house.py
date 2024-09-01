from fastapi import APIRouter, Body
from models.house_model import House

house_route = APIRouter()


@house_route.post("/")
def create_house(House: House = Body(...)):
    HouseModel.create(username=House.username, type=House.type, age=House.age, color=House.color)
    return House
    
@house_route.get("/{house_id}")
def read_house(house_id: int):
    try:
        house = HouseModel.get_by_id(house_id)
        return {"id": house.id, "username": house.username, "type": house.type, "age": house.age, "color": house.color}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="House not found")

@house_route.get("/")
def read_houses():
    houses = list(HouseModel.select())
    return houses

@house_route.put("/{house_id}")
def update_house(house_id: int):
    
        house = HouseModel.get_by_id(house_id)
        house.update(**house_data)
        return house

@house_route.delete("/{house_id}")
def delete_house(house_id: int):
    try:
        house = HouseModel.delete(HouseModel.id == house_id)
        return {"message": "House deleted"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="House not found")