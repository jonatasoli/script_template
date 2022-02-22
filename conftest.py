import pytest
from sqlalchemy.ext.asyncio import create_async_engine

from src.models import Base


@pytest.fixture()
async def create_db():
    url = 'sqlite+aiosqlite:///.test.db'
    engine = create_async_engine(url)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
