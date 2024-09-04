from sqlalchemy import Column, UUID, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from .model_class import Base as ModelBase


class BlogPosts(ModelBase):
    __tablename__ = "blog_posts"
    blog_post_id = Column(UUID(as_uuid=False), primary_key=True)
    blog_post_name = Column(String, unique=True)

    user_id = mapped_column(UUID(as_uuid=False), ForeignKey("users.user_id"))
    user = relationship("Users")
