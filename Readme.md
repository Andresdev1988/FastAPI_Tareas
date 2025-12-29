# FastAPI Tareas

Prueba técnica para la posición de **Desarrollador Backend Python**.

Este proyecto corresponde a una API REST desarrollada con **FastAPI**, diseñada como base para un sistema de gestión de tareas.  
La solución está orientada a ser **clara, mantenible, reproducible y fácil de ejecutar** en un entorno local desde cero.

---

## 📌 Estado actual del proyecto

En esta fase inicial, el proyecto incluye:

- Estructura base del backend
- Aplicación FastAPI funcional
- Endpoint de verificación de estado
- Documentación automática con Swagger
- Control de versiones con Git

Las funcionalidades completas (base de datos, autenticación, CRUD, etc.) se implementarán en las siguientes etapas.

---

## 🛠️ Tecnologías utilizadas

- **Python 3.11.8**
- **FastAPI** — Framework para la construcción de la API
- **Uvicorn** — Servidor ASGI
- **Git** — Control de versiones

---

## 📋 Requisitos previos

Antes de ejecutar el proyecto, asegúrese de tener instalado:

- Python **3.11.8**
- Git
- Windows, Linux o macOS

> ⚠️ La configuración de base de datos y Docker se realizará en etapas posteriores.

---

## 📂 Estructura del proyecto

```text
FastAPI_Tareas/
│
├── app/
│   ├── api/        # Endpoints de la API
│   ├── core/       # Configuración y componentes centrales
│   ├── db/         # Conexión a base de datos (pendiente)
│   ├── models/     # Modelos SQLAlchemy (pendiente)
│   ├── schemas/    # Esquemas Pydantic (pendiente)
│   ├── services/   # Lógica de negocio (pendiente)
│   └── main.py     # Punto de entrada de la aplicación
│
├── venv/           # Entorno virtual (no se versiona)
├── .gitignore
└── README.md