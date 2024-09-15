from flask import Flask, Blueprint
from .routes import route_blueprints


def register_route(app: Flask, blueprints: dict[str, Blueprint]):
    for key, bp in blueprints.items():
        app.register_blueprint(bp, name=key)


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    register_route(app=app, blueprints=route_blueprints)
    return app
