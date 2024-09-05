from flask_restful import Resource
from sqlalchemy import func
from sqlalchemy.orm import aliased
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
        review_alias = aliased(Review)
        query_results = (
            session.query(
                post_alias,
                user_alias,
                func.avg(review_alias.rating).label('average_rating')
            )
            .join(user_alias, user_alias.user_id == post_alias.user_id)
            .outerjoin(review_alias, review_alias.blog_post_id == post_alias.blog_post_id)
            .group_by(post_alias.blog_post_id)
        ).all()

        return [
            {
                'blog_post_id': str(blog_post.blog_post_id),
                'blog_post_name': blog_post.blog_post_name,
                'author': user.user_name,
                'average_rating': 0.0 if rating is None else rating

            }
            for blog_post, user, rating in query_results
        ]


class BlogPostResource(Resource):

    def __init__(self, **kwargs):
        self._db_instance = kwargs['db']

    def get(self, blog_post_id):
        session: Session = self._db_instance.session
        user_alias = aliased(Users)
        post_alias = aliased(BlogPosts)
        review_alias = aliased(Review)
        blog_post_query = session.query(
            post_alias,
            user_alias,
            func.avg(review_alias.rating).label('average_rating')
        ).filter_by(
            blog_post_id=blog_post_id
            ).join(
                user_alias, post_alias.user_id == user_alias.user_id
                ).outerjoin(
                    review_alias, review_alias.blog_post_id == post_alias.blog_post_id
                    ).first()

        if not blog_post_query[0] and not blog_post_query[1]:
            return {"message": f"blog post with blog_post_id: {blog_post_id} not found"}, 404
        else:
            blog_post, user, average_rating = blog_post_query
            return {
                'blog_post_id': str(blog_post.blog_post_id),
                'blog_post_name': blog_post.blog_post_name,
                'author': user.user_name,
                'average_rating': 0.0 if average_rating is None else average_rating
            }
