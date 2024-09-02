
from fastapi import APIRouter, Body
from models.phone_model import Phone
from database import PhoneModel

phone_route = APIRouter()


@phone_route.post("/")
def create_phone(Phone: Phone = Body(...)):
    PhoneModel.create(color=Phone.color, storage=Phone.storage, brand=Phone.brand, model=Phone.model)
    return Phone
    
    
@phone_route.get("/{phone_id}")
def read_phone(phone_id: int):
    try:
        phone = PhoneModel.get_by_id(phone_id)
        return {"id": phone.id, "color": phone.color, "storage": phone.storage, "brand": phone.brand, "model": phone.model}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Phone not found")

@phone_route.get("/")
def read_phones():
    phones = list(PhoneModel.select())
    return phones

@phone_route.put("/{phone_id}")
def update_phone(phone_id: int):

    phone = PhoneModel.get_by_id(phone_id)
    phone.update(**phone_data)
    return phone
    

@phone_route.delete("/{phone_id}")
def delete_phone(phone_id: int):
    try:
        phone = PhoneModel.delete(PhoneModel.id == phone_id)
        return {"message": "Phone deleted"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Phone not found")