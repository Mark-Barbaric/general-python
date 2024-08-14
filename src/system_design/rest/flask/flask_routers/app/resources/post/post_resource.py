from flask_restful import Resource
from .fake_post_db import POST_DB, POST_ARG_ID


class PostResource(Resource):
    def __init_(self, **kwargs):
        ...

    def get(self, post_id):
        if not POST_DB.get(post_id, None):
            return {'error_message': f"No post found with {POST_ARG_ID}: {post_id}"}, 404
        else:
            return POST_DB[post_id]
