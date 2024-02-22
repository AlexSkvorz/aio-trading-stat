from pydantic_settings import BaseSettings
from config.database_config import DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


class Settings(BaseSettings):
    DB_HOST: str = DB_HOST
    DB_PORT: int = DB_PORT
    DB_USER: str = DB_USER
    DB_PASS: str = DB_PASS
    DB_NAME: str = DB_NAME

    @property
    def DATABASE_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
)

async_session_factory = async_sessionmaker(async_engine)
