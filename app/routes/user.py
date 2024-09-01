from fastapi import APIRouter, Body
from app.models.user_model import User

user_route = APIRouter()


@user_route.post("/")
def create_user(user: User = Body(...)):
    try:
        return user
    except Exception as e:
        return {"error": str(e)}
    
@user_route.get("/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}

@user_route.get("/")
def read_users():
    return {"user_id": "user_id"}

@user_route.put("/{user_id}")
def update_user(user_id: int):
    return {"user_id": user_id}

@user_route.delete("/{user_id}")
def delete_user(user_id: int):
    return {"user_id": user_id}
