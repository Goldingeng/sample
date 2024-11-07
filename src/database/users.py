from sqlalchemy import select, BigInteger, Column, String
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from src.database.core import Base


class User(Base):
    __tablename__ = "users"
    __allow_unmapped__ = True

    id: int = Column(
        BigInteger,
        primary_key=True,
        index=True,
        unique=True
    )

    nickname: str = Column(String)

    @classmethod
    async def get(cls, session: AsyncSession, user_id: int) -> 'User':
        user_query = select(cls).filter(cls.id == user_id)
        try:
            return await session.scalar(user_query)
        except SQLAlchemyError as e:
            await session.rollback()
            raise e

    @classmethod
    async def add(cls, session: AsyncSession, user_id: int, nickname: str) -> 'User':
        user = await cls.get(session, user_id)
        try:
            if user is None:
                user = cls(id=user_id, nickname=nickname)
                session.add(user)
                await session.commit()
            return user
        except Exception as e:
            await session.rollback()
            raise e