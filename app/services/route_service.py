from app.dao import route_dao

async def get_all_routes():
    return {"routes": route_dao.read_routes()}

async def add_or_update_route(route_data):
    success, message = route_dao.save_or_update_route(route_data)
    return {"success": success, "message": message}
