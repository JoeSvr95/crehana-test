from pydantic import BaseModel
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Post


class PostModel(SQLAlchemyObjectType):
    class Meta:
        model = Post


class PostSchema(BaseModel):
    user_id: int
    title: str
    body: str
