from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Aplicación
    APP_NAME: str = "Gestor de Tareas"
    APP_ENV: str = "local"
    DEBUG: bool = True

    # Seguridad
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Base de datos
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()