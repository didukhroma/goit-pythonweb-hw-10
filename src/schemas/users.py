from pydantic import BaseModel, EmailStr, ConfigDict


class UserModel(BaseModel):
    username: str
    email: EmailStr
    password: str
    avatar: str


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    model_config = ConfigDict(from_attributes=True)


class RequestEmail(BaseModel):
    email: EmailStr


class TokenModel(BaseModel):
    access_token: str
