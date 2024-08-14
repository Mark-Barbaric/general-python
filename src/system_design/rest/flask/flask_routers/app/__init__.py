from .config import Config
from flask import Flask
from flask_restful import Api
from .resources import BaseResource, PostResource, PostListResource


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    api = Api(app)
    api.add_resource(BaseResource, '/')
    api.add_resource(PostListResource, '/posts')
    api.add_resource(PostResource, '/posts/<post_id>')
    return app
