from fastapi import APIRouter, Body
from app.models.store_model import Store


store_route = APIRouter()


@store_route.post("/")
def create_store(store: Store = Body(...)):
    try:
        return store
    except Exception as e:
        return {"error": str(e)}
    
@store_route.get("/{store_id}")
def read_store(store_id: int):
    return {"store_id": store_id}

@store_route.get("/")
def read_stores():
    return {"store_id": "store_id"}

@store_route.put("/{store_id}")
def update_store(store_id: int):
    return {"store_id": store_id}

@store_route.delete("/{store_id}")
def delete_store(store_id: int):
    return {"store_id": store_id}
