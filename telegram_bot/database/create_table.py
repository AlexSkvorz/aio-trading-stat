import asyncio
from database_connection import async_engine
from database_model import Base


async def async_create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    async_engine.echo = True


asyncio.run(async_create_tables())
