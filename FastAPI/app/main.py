from fastapi import FastAPI
from starlette.responses import RedirectResponse

# Base de datos
from database import database as connection
from routes.user_route import user_route
from routes.pet_route import pet_route
from routes.house_route import house_route
from routes.phone_route import phone_route
from routes.store_route import store_route
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Conectar a la base de datos si la conexión está cerrada
    if connection.is_closed():
        connection.connect()
    try:
        yield  # Aquí es donde se ejecutará la aplicación
    finally:
        # Cerrar la conexión cuando la aplicación se detenga
        if not connection.is_closed():
            connection.close()


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")


app.include_router(user_route, prefix="/api/users", tags=["users"])
# ----------------MASCOTAS----------------
app.include_router(pet_route, tags=["Mascotas"], prefix="/api/pets")

# ----------------CASAS----------------
app.include_router(house_route, tags=["Casas"], prefix="/api/houses")

# ----------------TELEFONOS----------------
app.include_router(phone_route, tags=["Telefonos"], prefix="/api/phones")

# ----------------TIENDAS----------------
app.include_router(store_route, tags=["Tiendas"], prefix="/api/stores")