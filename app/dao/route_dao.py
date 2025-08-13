import json
from pathlib import Path

ROUTES_FILE = Path("data/routes.json")
ROUTES_FILE.parent.mkdir(exist_ok=True)

def read_routes():
    if not ROUTES_FILE.exists():
        return []
    with open(ROUTES_FILE, "r") as f:
        return json.load(f)

def save_or_update_route(route_data):
    routes = read_routes()
    updated = False
    for idx, r in enumerate(routes):
        if r.get("path") == route_data.get("path") and r.get("method") == route_data.get("method"):
            routes[idx].update(route_data)
            updated = True
            break
    if not updated:
        route_data["id"] = max([r.get("id", 0) for r in routes], default=0) + 1
        routes.append(route_data)
    with open(ROUTES_FILE, "w") as f:
        json.dump(routes, f, indent=2)
    return True, "Updated" if updated else "Added"
