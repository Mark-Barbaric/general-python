from .config import Config
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from app.resources.blog_posts import BlogPostListResource, BlogPostResource
from app.resources.users import UserListResource
from app.model.model_class import Base


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    api = Api(app)
    db = SQLAlchemy(app,
                    model_class=Base)
    api.add_resource(BlogPostListResource,
                     '/posts',
                     resource_class_kwargs={'db': db})
    api.add_resource(BlogPostResource,
                     '/posts/<blog_post_id>',
                     resource_class_kwargs={'db': db})
    api.add_resource(UserListResource,
                     '/users',
                     resource_class_kwargs={'db': db})
    return app
