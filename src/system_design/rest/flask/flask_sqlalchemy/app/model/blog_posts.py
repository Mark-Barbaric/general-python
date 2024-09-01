from sqlalchemy import Column, UUID, String, ForeignKey
from sqlalchemy.orm import mapped_column
from .model_class import Base as ModelBase


class BlogPosts(ModelBase):
    __tablename__ = "blog_posts"
    blog_post_id = Column(UUID, primary_key=True)
    blog_post_name = Column(String, unique=True)
    user_id = mapped_column(ForeignKey("users.user_id"))

    def to_dict(self):
        return {
            'blog_post_id': self.blog_post_id,
            'blog_post_name': self.blog_post_name,
            'user_id': self.user_id
        }