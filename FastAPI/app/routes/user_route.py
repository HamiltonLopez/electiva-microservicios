from fastapi import APIRouter, Body
from models.user_model import User
from database import UserModel

user_route = APIRouter()


@user_route.get("/users")
def get_users():
    users = list(UserModel.select())
    return users


@user_route.get("/users/{user_id}")
def get_user(user_id: int):
    try:
        user = UserModel.get_by_id(user_id)
        return  {"id": user.id, "username": user.username, "email": user.email}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")

@user_route.post("/users")
def create_user(user: User = Body(...)):
    UserModel.create(username=user.username, email=user.email, password=user.password)
    return user


@user_route.put("/users/{user_id}")
def update_user(user_id: int, user_data: dict):

    user = UserModel.get_by_id(user_id)
    user.update(**user_data)
    return user


@user_route.delete("/users/delete/{user_id}")
def delete_user(user_id: int):
    try:
        user = UserModel.delete(UserModel.id == user_id)
        return {"message": "User deleted"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="User not found")