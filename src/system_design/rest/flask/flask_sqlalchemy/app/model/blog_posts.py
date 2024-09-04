from sqlalchemy import Column, UUID, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from .model_class import Base as ModelBase


class BlogPosts(ModelBase):
    __tablename__ = "blog_posts"
    blog_post_id = Column(UUID, primary_key=True)
    blog_post_name = Column(String, unique=True)

    user_id = mapped_column(UUID, ForeignKey("users.user_id"))
    user = relationship("Users")

    def to_dict(self):
        return {
            'blog_post_id': str(self.blog_post_id),
            'blog_post_name': self.blog_post_name,
            'user_id': str(self.user_id),
            'user_name': self.user.user_name
        }