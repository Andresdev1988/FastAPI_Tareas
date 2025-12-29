from fastapi import FastAPI

app = FastAPI(
    title="Prueba Técnica Backend - FastAPI",
    description="API para gestión de tareas",
    version="1.0.0"
)

@app.get("/salud")
def verificar_estado():
    return {"estado": "ok"}
