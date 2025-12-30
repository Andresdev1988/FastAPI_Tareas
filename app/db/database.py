from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings  # ← Importa directo, no get_settings()

# Construir DATABASE_URL con el driver correcto
DATABASE_URL = (
    f"postgresql+psycopg2://" 
    f"{settings.DB_USER}:"      
    f"{settings.DB_PASSWORD}@"  
    f"{settings.DB_HOST}:"      
    f"{settings.DB_PORT}/"      
    f"{settings.DB_NAME}"       
)

# Crear motor de base de datos
engine = create_engine(
    DATABASE_URL,
    echo=settings.DEBUG,  # ← MAYÚSCULAS
    pool_pre_ping=True,   # ← Verifica conexión antes de usar
    pool_size=5,          # ← Conexiones en el pool
    max_overflow=10       # ← Conexiones adicionales si se necesitan
)

# Crear sesión local
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base declarativa para modelos
Base = declarative_base()