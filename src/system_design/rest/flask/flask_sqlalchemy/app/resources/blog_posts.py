from flask_restful import Resource
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import Session
from ..model.blog_posts import BlogPosts
from ..model.users import Users


class BlogPostListResource(Resource):

    def __init__(self, **kwargs):
        self._db_instance = kwargs['db'] 
    
    def get(self):
        session: Session = self._db_instance.session
        blog_posts = session.query(BlogPosts).join(Users).options(joinedload(BlogPosts.user))
        return [blog_post.to_dict() for blog_post in blog_posts]


class BlogPostResource(Resource):
    def get(self, blog_post_id):
        return self._db_session.query.filter_by(blog_post_id=blog_post_id)
