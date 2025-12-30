# 📝 Sistema de Gestión de Tareas - FastAPI

> Prueba técnica para la posición de **Desarrollador Backend Python**

Una API REST construida con FastAPI que sirve como base para un sistema completo de gestión de tareas. El proyecto está diseñado pensando en la simplicidad: cualquier desarrollador debería poder clonarlo y tenerlo corriendo en minutos.

---

## 🎯 ¿Qué encontrarás aquí?

Este es un proyecto en desarrollo activo. Por ahora incluye:

✅ Arquitectura base bien estructurada y escalable  
✅ API funcional con FastAPI  
✅ Endpoint de health check  
✅ Documentación interactiva (Swagger UI)  


**Próximamente:** Base de datos PostgreSQL, autenticación JWT, CRUD completo de tareas, tests automatizados y contenedorización con Docker.

---

## 🚀 Stack Tecnológico

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| Python | 3.11.8 | Lenguaje base |
| FastAPI | latest | Framework web moderno y rápido |
| Uvicorn | latest | Servidor ASGI de alto rendimiento |
| Git | latest | Control de versiones |

---

## 📦 Requisitos

Para ejecutar este proyecto necesitas tener instalado:

### Herramientas principales

- **Python 3.11.8** → [Descargar aquí](https://www.python.org/downloads/)
- **Git** → [Descargar aquí](https://git-scm.com/downloads)
- **Docker Desktop** → [Descargar aquí](https://www.docker.com/products/docker-desktop/)

### ¿Por qué Docker?

Este proyecto usa Docker para ejecutar PostgreSQL, lo que garantiza:
- ✅ Entorno reproducible en cualquier sistema operativo
- ✅ No necesitas instalar PostgreSQL manualmente
- ✅ Fácil setup con un solo comando

Docker Desktop incluye:
- Docker Engine (motor de contenedores)
- Docker Compose (orquestación de servicios)

**Nota para Windows:** Docker Desktop instalará y configurará WSL 2 automáticamente si no lo tienes.

### Otras herramientas

- Un editor de código (recomiendo VS Code o PyCharm)
- Terminal/CMD/PowerShell/Git Bash

Compatible con Windows 10/11, Linux y macOS.

---

### ✅ Verificar instalación

Ejecuta estos comandos para confirmar que todo está instalado correctamente:
```bash
# Python
python --version  # Debe mostrar: Python 3.11.8

# Git
git --version     # Ejemplo: git version 2.43.0

# Docker
docker --version  # Ejemplo: Docker version 24.0.7
docker compose version  # Ejemplo: Docker Compose version v2.23.0
```

Si todos los comandos funcionan, puedes continuar con la instalación del proyecto.

---

## 🗂️ Arquitectura del Proyecto

```
FastAPI_Tareas/
│
├── app/
│   ├── api/           # 🛣️  Rutas y endpoints
│   ├── core/          # ⚙️  Configuración global
│   ├── db/            # 🗄️  Conexión a BD (próximamente)
│   ├── models/        # 📊 Modelos de datos (próximamente)
│   ├── schemas/       # 📋 Validación con Pydantic (próximamente)
│   ├── services/      # 🧠 Lógica de negocio (próximamente)
│   └── main.py        # 🚪 Punto de entrada
│
├── venv/              # 🔒 Entorno virtual (no versionado)
├── .gitignore
├── requirements.txt   # 📌 Dependencias del proyecto
└── README.md          # 📖 Estás aquí
```

---

## 🎬 Puesta en Marcha de instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/Andresdev1988/FastAPI_Tareas.git
cd FastAPI_Tareas
```

### 2. Crea tu entorno virtual

Esto mantiene las dependencias aisladas y evita conflictos con otros proyectos.

```bash
python -m venv venv
```

### 3. Activa el entorno virtual

**En Windows (PowerShell/CMD):**
```bash
venv\Scripts\activate
```

**En Linux/macOS:**
```bash
source venv/bin/activate
```

💡 Sabrás que funcionó cuando veas `(venv)` al inicio de tu línea de comando.

### 4. Actualiza pip (recomendado)

```bash
python -m pip install --upgrade pip
```

### 5. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 6. Configurar variables de entorno / Crear copia de la plantila env.example

```bash
cp .env.example .env  
```


### 7. ¡Ejecuta la aplicación!

```bash
uvicorn app.main:app --reload
```

Si todo salió bien, verás algo como esto:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
```

---

## ✅ Verifica que todo funcione

### 🏥 Health Check

Abre tu navegador y ve a:
```
http://127.0.0.1:8000/salud
```

Deberías ver:
```json
{
  "estado": "ok"
}
```

### 📚 Documentación Interactiva

FastAPI genera automáticamente una documentación hermosa y funcional:

**Swagger UI (recomendado):**  
👉 http://127.0.0.1:8000/docs

Desde aquí puedes probar todos los endpoints directamente desde tu navegador. ¡No necesitas Postman!

**ReDoc (alternativa):**  
👉 http://127.0.0.1:8000/redoc

---

## 🐘 Levantar la Base de Datos

Este proyecto usa PostgreSQL en Docker. Para iniciar la base de datos:
```bash
docker compose up -d
```

Este comando:
- Descarga la imagen de PostgreSQL (solo la primera vez)
- Crea el contenedor `postgres_fastapi_tareas`
- Levanta PostgreSQL en segundo plano
- Expone el puerto `5432` en `localhost`

### Verificar que esté corriendo
```bash
docker compose ps
```

Debes ver el contenedor con estado `Up`.

### Comandos útiles
```bash
# Ver logs
docker compose logs -f

# Detener PostgreSQL
docker compose stop

# Detener y eliminar contenedor (mantiene datos)
docker compose down

# Reiniciar
docker compose restart
```

## 🧠 Decisiones de Diseño

**¿Por qué FastAPI?**  
Es uno de los frameworks más rápidos de Python, tiene validación automática de datos, genera documentación automáticamente y su sintaxis es muy intuitiva.

**¿Por qué Uvicorn?**  
Es un servidor ASGI ultra rápido, perfecto para aplicaciones asíncronas. Además, el flag `--reload` hace que el desarrollo sea mucho más ágil.

**¿Por qué venv?**  
Los entornos virtuales son esenciales para evitar conflictos entre dependencias de diferentes proyectos. Es una práctica estándar en Python.

**Estructura modular:**  
Cada carpeta tiene una responsabilidad clara. Esto hace que el código sea más fácil de mantener, testear y escalar.

---

## 🔄 Próximos Pasos

- [ ] Integración con PostgreSQL
- [ ] Sistema de autenticación con JWT
- [ ] CRUD completo de tareas
- [ ] Tests unitarios y de integración
- [ ] Dockerización del proyecto
- [ ] CI/CD con GitHub Actions
- [ ] Deploy en producción

---

## 🤝 Contribuciones

Este proyecto es parte de una prueba técnica, pero las sugerencias son bienvenidas. Si encuentras algún bug o tienes ideas de mejora, no dudes en abrir un issue.

---

## 👨‍💻 Autor

**Andrés** - Desarrollador Backend  
📧 [a.canorave@gmail.com]  | 🔗 [LinkedIn](https://www.linkedin.com/in/andres-cano-rave-desarrollador-full-stack/) | 💻 [GitHub](https://github.com/devrave)

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.

---

<p align="center">Hecho con ❤️ y FastAPI</p>