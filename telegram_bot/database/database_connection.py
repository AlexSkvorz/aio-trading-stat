import asyncio
import socket
from sqlalchemy import MetaData
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from config.database_config import POSTGRES_CONNECTION
from telegram_bot.database.database_model import Base


class DatabaseManager:
    def __init__(self, pg_connection):
        self.engine = create_async_engine(pg_connection, echo=True)
        self.Session = async_sessionmaker(self.engine, expire_on_commit=False, echo=True, class_=AsyncSession)
        self.metadata = MetaData()

    async def init_models(self):
        try:
            async with self.engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            self.engine.echo = True
        except socket.gaierror:
            print("Не удалось разрешить имя хоста в строке подключения к базе данных")
            raise

    async def async_init(self):
        await self.init_models()


try:
    db_manager = DatabaseManager(POSTGRES_CONNECTION)
    asyncio.run(db_manager.init_models())
except (OperationalError, socket.gaierror):
    print("Не удалось инициализировать DatabaseManager")
