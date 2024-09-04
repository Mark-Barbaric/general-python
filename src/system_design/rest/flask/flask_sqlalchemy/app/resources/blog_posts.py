from flask_restful import Resource
from sqlalchemy.orm import joinedload, aliased
from sqlalchemy.orm.session import Session
from ..model.blog_posts import BlogPosts
from ..model.users import Users
from ..model.review import Review


class BlogPostListResource(Resource):

    def __init__(self, **kwargs):
        self._db_instance = kwargs['db'] 
    
    def get(self):
        session: Session = self._db_instance.session
        user_alias = aliased(Users)
        post_alias = aliased(BlogPosts)
        review_alias = alised(Review)
        query_results = (
            session.query(BlogPosts).join(Users).options(joinedload(BlogPosts.user))
        )
        return [result.to_dict() for result in query_results]


class BlogPostResource(Resource):
    def get(self, blog_post_id):
        return self._db_session.query.filter_by(blog_post_id=blog_post_id)
