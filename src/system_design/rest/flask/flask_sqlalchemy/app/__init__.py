import argparse
from flask import Flask
from flask_restful import Api
from .resources.blog_posts import BlogPostListResource, BlogPostResource
from .resources.users import UserListResource
from .extensions import db
from .config import Config



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    api = Api(app)
    db.init_app(app)
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


def main():    
    parser = argparse.ArgumentParser(description='Run the Flask application.')
    parser.add_argument('--config', help='The configuration to use.')
    parser.add_argument('--host', default='127.0.0.1', help='The host to listen on.')
    parser.add_argument('--port', default=5000, type=int, help='The port to listen on.')
    parser.add_argument('--debug', action='store_true', help='Run in debug mode.')

    args = parser.parse_args()
    app = create_app(args.config)

    app.run(host=args.host, port=args.port, debug=args.debug)


if __name__ == "__main__":
    main()
