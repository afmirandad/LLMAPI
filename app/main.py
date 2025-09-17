
from fastapi import FastAPI
from app.routes import inventario

# Configuración de la documentación en español
app = FastAPI(
	title="API de Inventario de Activos",
	description="API para la gestión, consulta y administración de activos de información. Permite operaciones CRUD y búsqueda avanzada.",
	version="1.0.0",
	docs_url="/docs",
	redoc_url="/redoc",
	openapi_tags=[
		{
			"name": "Inventario",
			"description": "Operaciones sobre el inventario de activos de información."
		}
	]
)

app.include_router(inventario.router)
