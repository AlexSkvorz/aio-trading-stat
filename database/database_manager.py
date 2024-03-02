import socket
import logging
import asyncpg
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from database.database_tables import Base


class DatabaseManager:
    def __init__(self, pg_connection):
        self.engine = create_async_engine(pg_connection)
        self.Session = async_sessionmaker(self.engine, expire_on_commit=False, echo=True, class_=AsyncSession)
        self.metadata = MetaData()

    async def init_models(self):
        try:
            async with self.engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
        except ConnectionRefusedError:
            logging.critical("The remote computer rejected this network connection")
        except socket.gaierror:
            logging.critical("Failed to resolve the hostname in the database connection string")
        except asyncpg.exceptions.ConnectionDoesNotExistError:
            logging.critical("The connection was closed during the operation")

    async def async_init(self):
        await self.init_models()
