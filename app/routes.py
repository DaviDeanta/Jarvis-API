from fastapi import APIRouter, Body
from app.services.routes_service import get_routes, save_route

router = APIRouter()

@router.get("/routes", summary="Listar rotas")
def list_routes():
    return {"routes": get_routes()}

@router.post("/routes", summary="Salvar nova rota")
def post_route(data: dict = Body(...)):
    return save_route(data)
