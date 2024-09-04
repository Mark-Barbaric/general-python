from sqlalchemy import UUID, Column, String
from .model_class import Base as ModelBase


class Users(ModelBase):
    __tablename__ = "users"
    user_id = Column(UUID(as_uuid=False), primary_key=True)
    user_name = Column(String, unique=True)
