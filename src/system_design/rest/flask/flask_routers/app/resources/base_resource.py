from flask_restful import Resource


class BaseResource(Resource):
    def get(self):
        return {'message': 'Hellow World'}
