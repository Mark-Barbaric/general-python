from .model_class import Base as ModelBase
from sqlalchemy import UUID, Column, Float, ForeignKey
from sqlalchemy.orm import mapped_column, relationship


class Review(ModelBase):
    __tablename__ = "reviews"
    review_id = Column(UUID, primary_key=True)
    rating = Column(Float)
    blog_post_id = mapped_column(UUID, ForeignKey('blog_posts.blog_post_id'))
    blog_post = relationship('BlogPosts')
    user_id = mapped_column(UUID, ForeignKey('users.user_id'))
    users = relationship('Users')
