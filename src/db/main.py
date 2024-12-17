from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.declarative import declarative_base
from src.config import Config

# create the engine
enginer = AsyncEngine(create_engine(url=Config.DATABASE_URL, echo=True))
Base = declarative_base()


# connecting to database using lifespan event
async def init_db():
    async with enginer.begin() as conn:
        from src.books.models import Book
        await conn.run_sync(SQLModel.metadata.create_all)