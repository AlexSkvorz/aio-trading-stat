import asyncio
import socket
import logging
import asyncpg
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from config.database_config import POSTGRES_CONNECTION
from database.database_manager import Base
from config.logging_config import configure_logging


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
        except ConnectionRefusedError:
            logging.fatal("Удаленный компьютер отклонил это сетевое подключение")
        except socket.gaierror:
            logging.fatal("Не удалось разрешить имя хоста в строке подключения к базе данных")
        except asyncpg.exceptions.ConnectionDoesNotExistError:
            logging.fatal("Соединение было закрыто во время операции")

    async def async_init(self):
        await self.init_models()


configure_logging()
db_manager = DatabaseManager(POSTGRES_CONNECTION)
asyncio.run(db_manager.init_models())
