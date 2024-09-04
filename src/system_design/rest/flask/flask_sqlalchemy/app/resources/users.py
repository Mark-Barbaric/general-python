from flask_restful import Resource
from ..model.users import Users


class UserListResource(Resource):
    def __init__(self, **kwargs):
        self._db_session = kwargs['db']

    def get(self):
        users = self._db_session.session.query(Users).all()

        if len(users) > 0:
            return [user.to_dict() for user in users]
        else:
            return []


class UserResource(Resource):
    def __init__(self, **kwargs):
        self._db_instance = kwargs['db']

    def get(self, user_id):
        user = self._db_instance.session.query(Users).get(user_id)