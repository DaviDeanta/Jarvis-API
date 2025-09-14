from app.dao import route_dao
from app.models import RouteModel
from typing import Dict, Any


async def get_all_routes() -> Dict[str, Any]:
    """Get all routes"""
    try:
        routes = route_dao.read_routes()
        return {"routes": routes, "total": len(routes)}
    except Exception as e:
        return {"error": str(e), "routes": []}


async def add_or_update_route(route_data: Dict[str, Any]) -> Dict[str, Any]:
    """Add or update route with validation"""
    try:
        # Validate data
        route = RouteModel(**route_data)
        
        # Save to DAO
        success, message = route_dao.save_or_update_route(route.dict())
        return {"success": success, "message": message}
    except Exception as e:
        return {"success": False, "error": str(e)}


async def update_route(route_id: int, route_data: Dict[str, Any]) -> Dict[str, Any]:
    """Update specific route by ID"""
    try:
        # Validate data
        route = RouteModel(**route_data)
        
        # Get existing route
        routes = route_dao.read_routes()
        route_index = next((i for i, r in enumerate(routes) if r.get("id") == route_id), None)
        
        if route_index is None:
            return {"success": False, "error": f"Route with ID {route_id} not found"}
        
        # Update route
        routes[route_index].update(route.dict())
        route_dao.save_routes(routes)
        
        return {"success": True, "message": f"Route {route_id} updated successfully"}
    except Exception as e:
        return {"success": False, "error": str(e)}


async def delete_route(route_id: int) -> Dict[str, Any]:
    """Delete specific route by ID"""
    try:
        routes = route_dao.read_routes()
        route_index = next((i for i, r in enumerate(routes) if r.get("id") == route_id), None)
        
        if route_index is None:
            return {"success": False, "error": f"Route with ID {route_id} not found"}
        
        # Remove route
        deleted_route = routes.pop(route_index)
        route_dao.save_routes(routes)
        
        return {"success": True, "message": f"Route {route_id} deleted successfully"}
    except Exception as e:
        return {"success": False, "error": str(e)}
