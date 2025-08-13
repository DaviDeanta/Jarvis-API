from fastapi import FastAPI
from app.routes.route_routes import router as route_router  # Caminho correto

app = FastAPI()
app.include_router(route_router)  # Inclui o router