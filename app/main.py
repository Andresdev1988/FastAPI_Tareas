from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME
)

@app.get("/salud")
def verificar_estado():
    return {"estado": "ok"}
