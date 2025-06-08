from typing import Self

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import User
from src.schemas.users import UserModel


class UserRepository:
    def __init__(self: Self, session: AsyncSession):
        self.db = session

    async def get_user_by_email(self: Self, user_email: str) -> User | None:
        stmt = select(User).where(User.email == user_email)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def create_user(self: Self, body: UserModel, avatar) -> User | None:
        user = User(
            **body.model_dump(exclude_unset=True, exclude={"password"}),
            hashed_password=body.password,
            avatar=avatar,
        )
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def change_confirmed_email(self: Self, user_email: str) -> None:
        user = await self.get_user_by_email(user_email)
        user.confirmed_email = True
        await self.db.commit()

    async def update_token(self: Self, access_token: str) -> None:
        pass
        # user = await self.get_user_by_email(user_email)
        # user.access_token = True
        # await self.db.commit()
