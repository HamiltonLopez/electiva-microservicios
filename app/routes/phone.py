
from fastapi import APIRouter, Body
from app.models.phone_model import Phone


phone_route = APIRouter()


@phone_route.post("/")
def create_phone(Phone: Phone = Body(...)):
    try:
        return phone
    except Exception as e:
        return {"error": str(e)}
    
@phone_route.get("/{phone_id}")
def read_phone(phone_id: int):
    return {"phone_id": phone_id}

@phone_route.get("/")
def read_phones():
    return {"phone_id": "phone_id"}

@phone_route.put("/{phone_id}")
def update_phone(phone_id: int):
    return {"phone_id": phone_id}

@phone_route.delete("/{phone_id}")
def delete_phone(phone_id: int):
    return {"phone_id": phone_id}