from fastapi import APIRouter
from app.controllers import route_controller
from app.models import RouteModel

router = APIRouter(prefix="/api/v1", tags=["routes"])

@router.get("/routes", summary="Get all routes")
async def get_routes():
    """Get all available routes"""
    return await route_controller.get_routes()

@router.post("/routes", summary="Add new route")
async def add_route(route_data: RouteModel):
    """Add a new route to the system"""
    return await route_controller.add_route(route_data)

@router.put("/routes/{route_id}", summary="Update route")
async def update_route(route_id: int, route_data: RouteModel):
    """Update an existing route by ID"""
    return await route_controller.update_route(route_id, route_data)

@router.delete("/routes/{route_id}", summary="Delete route")
async def delete_route(route_id: int):
    """Delete a route by ID"""
    return await route_controller.delete_route(route_id)
