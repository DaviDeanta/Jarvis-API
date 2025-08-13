import json
from app.config import settings

def get_routes():
    try:
        with open(settings.ROUTES_PATH, "r") as file:
            return json.load(file)
    except Exception as e:
        return {"error": str(e)}

def save_route(data: dict) -> dict:
    try:
        with open(settings.ROUTES_PATH, "r") as file:
            routes = json.load(file)

        existing = next((r for r in routes if r["path"] == data["path"] and r["method"] == data["method"]), None)

        if existing:
            for k in data:
                if k != "id":
                    existing[k] = data[k]
            msg = f"Rota '{data['method']} {data['path']}' atualizada."
        else:
            next_id = max([r["id"] for r in routes], default=0) + 1
            data["id"] = next_id
            routes.append(data)
            msg = f"Rota '{data['method']} {data['path']}' adicionada com id {next_id}."

        with open(settings.ROUTES_PATH, "w") as file:
            json.dump(routes, file, indent=2)

        return {"success": True, "message": msg}
    except Exception as e:
        return {"success": False, "error": str(e)}