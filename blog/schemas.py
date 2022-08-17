from pydantic import BaseModel
from typing import Optional, List, Union


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                "title": "Gold",
                "body": "Hello World",
            }
        }


class UpdateBlog(BaseModel):
    title: Optional[str]
    body: Optional[str]


class User(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    # id: int
    name: str
    email: str
    items: List[Blog] = []

    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    owner: ShowUser

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
