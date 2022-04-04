from sqlalchemy import Column, Integer, String

from db.db_conf import Base


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer)
    title = Column(String)
    body = Column(String)
