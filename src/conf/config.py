from pydantic import ConfigDict
from pydantic_settings import BaseSettings
from typing import Self


class Settings(BaseSettings):
    # DB
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: str
    POSTGRES_HOST: str
    # DB_URL: str = "postgresql+asyncpg://postgres:567234@postgres_db:5432/hw10"
    # JWT
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_SECONDS: int = 3600

    # CONFIG
    model_config = ConfigDict(
        extra="ignore", env_file=".env", env_file_encoding="utf-8", case_sensitive=True
    )

    @property
    def database_url(self: Self):
        return "postgresql+asyncpg://postgres:567234@localhost:5432/postgres"
        # return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


# for docker compose


settings = Settings()
