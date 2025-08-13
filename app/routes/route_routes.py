from fastapi import APIRouter
from app.controllers import route_controller

router = APIRouter()

router.get("/routes")(route_controller.get_routes)
router.post("/routes")(route_controller.add_route)
