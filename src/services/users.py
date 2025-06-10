from typing import Self
from sqlalchemy.ext.asyncio import AsyncSession
from libgravatar import Gravatar

from src.repository.users import UserRepository
from src.schemas.users import UserCreate


class UserService:
    def __init__(self: Self, db: AsyncSession):
        self.repository = UserRepository(db)

    async def create_user(self: Self, user: UserCreate):
        avatar = None
        try:
            g = Gravatar(user.email)
            avatar = g.get_image()
        except Exception as e:
            print(e)
        return await self.repository.create_user(user, avatar)

    async def get_user_by_email(self: Self, email: str):
        return await self.repository.get_user_by_email(email)
