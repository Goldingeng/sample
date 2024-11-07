from __future__ import annotations
from typing import Type, Optional
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncAttrs, AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase
from src.config import BD_TEST


engine: AsyncEngine = create_async_engine(BD_TEST, future=True, echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(AsyncAttrs, DeclarativeBase):
    pass


def table(table_name: str) -> Optional[Type[Base]]:
    """Возвращает модель SQLAlchemy по имени таблицы."""
    for c in Base.__subclasses__():
        if c.__tablename__ == table_name:
            return c
    raise ValueError(f"Таблица с именем {table_name} не найдена.")


async def setup_database() -> None:
    """Создание всех таблиц в базе данных."""
    from . import (
        users
    )

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
