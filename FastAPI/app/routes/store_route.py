from fastapi import APIRouter, Body
from models.store_model import Store


store_route = APIRouter()


@store_route.post("/")
def create_store(store: Store = Body(...)):
    StoreModel.create(name=store.name, location=store.location, phone=store.phone)
    return store
    
@store_route.get("/{store_id}")
def read_store(store_id: int):
    try:
        store = StoreModel.get_by_id(store_id)
        return {"id": store.id, "name": store.name, "location": store.location, "phone": store.phone}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Store not found")

@store_route.get("/")
def read_stores():
    stores = list(StoreModel.select())
    return stores

@store_route.put("/{store_id}")
def update_store(store_id: int):
            
                store = StoreModel.get_by_id(store_id)
                store.update(**store_data)
                return store

@store_route.delete("/{store_id}")
def delete_store(store_id: int):
    return {"store_id": store_id}
