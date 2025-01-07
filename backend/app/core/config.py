from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Healthcare Chatbot API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api"
    
    # Database settings
    DATABASE_URL: str = "sqlite+aiosqlite:///healthcare.db"
    
    class Config:
        case_sensitive = True

settings = Settings()
