from sqlalchemy import func
from sqlalchemy.orm import Session, aliased
from .abstract_repository import AbstractRepository
from ..domain.blog_posts import BlogPosts
from ..domain.users import Users
from ..domain.review import Review


class BlogPostRepository(AbstractRepository):
    def __init__(self, session):
        self._session: Session = session

    def get(self, blog_post_id) -> Users:
        user_alias = aliased(Users)
        post_alias = aliased(BlogPosts)
        review_alias = aliased(Review)
        blog_post_query = self._session.query(
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
        return blog_post_query

    def get_list(self) -> list[Users]:        
        user_alias = aliased(Users)
        post_alias = aliased(BlogPosts)
        review_alias = aliased(Review)
        query_results = (
            self._session.query(
                post_alias,
                user_alias,
                func.avg(review_alias.rating).label('average_rating')
            )
            .join(user_alias, user_alias.user_id == post_alias.user_id)
            .outerjoin(review_alias, review_alias.blog_post_id == post_alias.blog_post_id)
            .group_by(post_alias.blog_post_id)
        ).all()
        return query_results

    def add(self) -> None:
        raise NotImplementedError
