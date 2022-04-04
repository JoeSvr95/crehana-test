from pydantic import BaseModel
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Comment


class CommentModel(SQLAlchemyObjectType):
    class Meta:
        model = Comment


class CommentSchema(BaseModel):
    post_id: int
    name: str
    email: str
    body: str
