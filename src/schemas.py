from pydantic import BaseModel


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: str
    password: str


class UserPublic(BaseModel):
    username: str
    email: str


class UserList(BaseModel):
    users: list[UserPublic]