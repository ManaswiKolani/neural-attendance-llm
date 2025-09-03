from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./app.db"
    CORS_ORIGINS: list[str] = ["http://localhost:5173", "http://127.0.0.1:5173"]
    FACE_THRESHOLD: float = 0.6
    MODEL_VERSION: str = "nn_v1"

settings = Settings()
