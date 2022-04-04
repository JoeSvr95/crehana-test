from ast import For
from sqlalchemy import Column, Integer, String, ForeignKey

from db.db_conf import Base


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True)
    postId = Column(Integer, ForeignKey("post.id"), nullable=False)
    name = Column(String)
    email = Column(String)
    body = Column(String)
