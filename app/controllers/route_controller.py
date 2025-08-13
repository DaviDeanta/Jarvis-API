from fastapi import Request
from app.services import route_service

async def get_routes():
    return await route_service.get_all_routes()

async def add_route(request: Request):
    body = await request.json()
    return await route_service.add_or_update_route(body)
