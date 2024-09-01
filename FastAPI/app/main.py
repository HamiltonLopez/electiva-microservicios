from fastapi import FastAPI, Body;
from app.models.user_model import User;
from starlette.responses import RedirectResponse
from databases import Database as connection
from contextlib import closing

from app.routes.user import user_route
from app.routes.pet import pet_route
from app.routes.house import house_route
from app.routes.phone import phone_route
from app.routes.store import store_route


@asynccontextmanager
async def get_connection():
    connection = await connection()
    try:
        yield connection
    finally:
        connection.close()
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

