from fastapi import Request, HTTPException
from app.services import route_service
from app.models import RouteModel
from typing import Dict, Any


async def get_routes() -> Dict[str, Any]:
    """Get all routes"""
    result = await route_service.get_all_routes()
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result


async def add_route(route_data: RouteModel) -> Dict[str, Any]:
    """Add new route"""
    try:
        result = await route_service.add_or_update_route(route_data.dict())
        if not result.get("success", False):
            raise HTTPException(status_code=400, detail=result.get("error", "Invalid data"))
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


async def update_route(route_id: int, route_data: RouteModel) -> Dict[str, Any]:
    """Update existing route"""
    try:
        result = await route_service.update_route(route_id, route_data.dict())
        if not result.get("success", False):
            raise HTTPException(status_code=404, detail=result.get("error", "Route not found"))
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


async def delete_route(route_id: int) -> Dict[str, Any]:
    """Delete route"""
    try:
        result = await route_service.delete_route(route_id)
        if not result.get("success", False):
            raise HTTPException(status_code=404, detail=result.get("error", "Route not found"))
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
