import asyncio
from sqlalchemy.ext.asyncio import async_sessionmaker,create_async_engine,AsyncSession
from .dbconfig import settings

async_engine = create_async_engine(url=settings.DB_URL,echo=True)

session = async_sessionmaker(async_engine)

async def get_session() -> AsyncSession:
    async with session() as sess:
        yield sess