import pytest
import uuid
from sqlalchemy import create_engine
from src.system_design.rest.flask.flask_sqlalchemy.app.config import TestConfig
from src.system_design.rest.flask.flask_sqlalchemy.app.extensions import db as _db
from src.system_design.rest.flask.flask_sqlalchemy.app.model.users import Users
from src.system_design.rest.flask.flask_sqlalchemy.app.model.blog_posts import BlogPosts
from src.system_design.rest.flask.flask_sqlalchemy.app.model.review import Review
from src.system_design.rest.flask.flask_sqlalchemy.app import create_app

@pytest.fixture
def flask_sql_alchemy_app():
    app = create_app(TestConfig)
    yield app


@pytest.fixture
def setup_test_database(flask_sql_alchemy_app):
    with flask_sql_alchemy_app.app_context():
        _db.create_all()

        user_uuid1 = uuid.uuid4()
        user_uuid2 = uuid.uuid4()
        user_uuid3 = uuid.uuid4()
        blog_post_uuid1 = uuid.uuid4()
        blog_post_uuid2 = uuid.uuid4()

        _db.session.add_all([
            Users(user_id=user_uuid1, user_name='mark'),
            Users(user_id=user_uuid2, user_name='john'),
            Users(user_id=user_uuid3, user_name='peter')
        ])
        
        _db.session.add_all([
            BlogPosts(blog_post_id=blog_post_uuid1, blog_post_name='Post 1', user_id=user_uuid1),
            BlogPosts(blog_post_id=blog_post_uuid2, blog_post_name='Post 2', user_id=user_uuid1)
        ])
    
        _db.session.add_all([
            Review(review_id=uuid.uuid4(), rating=4.0, blog_post_id=blog_post_uuid1, user_id=user_uuid2),
            Review(review_id=uuid.uuid4(), rating=3.5, blog_post_id=blog_post_uuid1, user_id=user_uuid3)
        ])

        _db.session.commit()

        yield _db

        _db.session.remove()
        _db.drop_all()


@pytest.fixture(scope='function')
def flask_sql_alchemy_test_client(flask_sql_alchemy_app, setup_test_database):
    return flask_sql_alchemy_app.test_client()
