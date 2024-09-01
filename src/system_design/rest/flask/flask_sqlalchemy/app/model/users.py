from sqlalchemy import UUID, Column, String
from .model_class import Base as ModelBase

class Users(ModelBase):
    __tablename__ = "users"
    user_id = Column(UUID, primary_key=True)
    user_name = Column(String, unique=True)

    def to_dict(self):
        return {
            'user_id' : str(self.user_id),
            'user_name' : self.user_name
        }