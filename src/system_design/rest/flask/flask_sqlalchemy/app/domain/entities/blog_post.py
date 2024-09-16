from pydantic import BaseModel


class BlogPostEntity(BaseModel):
    blog_post_id: str
    blog_post_name: str
    author: str
    average_rating: float = 0.0