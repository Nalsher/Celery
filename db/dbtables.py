from sqlalchemy.orm import mapped_column,Mapped,DeclarativeBase
from sqlalchemy import MetaData
from sqlalchemy import UUID
from sqlalchemy.schema import CreateTable,DropTable
from .dbengine import async_engine

class Base(DeclarativeBase):
    pass

Meta = MetaData()

Base.metadata = Meta
class users(Base):
    __tablename__ = "users"
    uuid: Mapped[str] = mapped_column(UUID,primary_key=True)
    name: Mapped[str]
    login: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    token: Mapped[str] = mapped_column(nullable=True)
    info: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=False)
async def create_table():
    async with async_engine.begin() as eng:
        await eng.run_sync(Base.metadata.create_all)
async def drop_table():
    async with async_engine.begin() as eng:
        await eng.run_sync(Base.metadata.drop_all)