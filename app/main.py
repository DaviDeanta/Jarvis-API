from fastapi import FastAPI
from app.routes import router
from app.config import settings

app = FastAPI(title="Jarvis Local API", version="1.0.0")
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Jarvis Local API está rodando!"}
