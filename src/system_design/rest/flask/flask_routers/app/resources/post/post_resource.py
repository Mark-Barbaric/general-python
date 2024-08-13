from flask_restful import Resource, reqparse
from .fake_post_db import POST_DB, POST_ARG_ID

def PostResource(Resource):
    def __init_(self, **kwargs):
        ...

    def get(self):
        post_resource_rq = reqparse.RequestParser()
        post_resource_rq.add_argument(POST_ARG_ID,
                                      help='post_id cannot be blank',
                                      required=True,
                                      action='append')
        args = post_resource_rq.parse_args()
        requested_post_id = args[POST_ARG_ID]

        if not POST_DB.get(requested_post_id, None):
            return {'error_message': f"No post found with {POST_ARG_ID}: {requested_post_id}"}
        else:
            return POST_DB[requested_post_id]

        
        