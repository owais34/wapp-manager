from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    MONGO_URI: str
    MONGO_DB: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ALGORITHM: str = "HS256"
    LOG_LEVEL: str = "DEBUG"

    class Config:
        env_file = ".env"


SETTINGS = Settings()