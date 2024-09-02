from fastapi import FastAPI, Body;
from app.models.user_model import User;
from starlette.responses import RedirectResponse

from app.routes.user_router import user_route
from app.routes.pet_router import pet_route
from app.routes.house_router import house_route
from app.routes.phone_router import phone_route
from app.routes.store_router import store_route

app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


# ----------------USUARIOS----------------
app.include_router(user_route, tags=["Usuarios"], prefix="/users")

# ----------------MASCOTAS----------------
app.include_router(pet_route, tags=["Mascotas"], prefix="/pets")

# ----------------CASAS----------------
app.include_router(house_route, tags=["Casas"], prefix="/houses")

# ----------------TELEFONOS----------------
app.include_router(phone_route, tags=["Telefonos"], prefix="/phones")

# ----------------TIENDAS----------------
app.include_router(store_route, tags=["Tiendas"], prefix="/stores")

