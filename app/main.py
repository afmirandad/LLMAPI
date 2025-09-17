from fastapi import FastAPI
from app.routes import inventario

app = FastAPI()

app.include_router(inventario.router)
