from flask_restful import Resource
from sqlalchemy.orm import aliased
from ..model.users import Users


class UserListResource(Resource):
    def __init__(self, **kwargs):
        self._db_session = kwargs['db']

    def get(self):
        users_query = self._db_session.session.query(Users).all()

        return [
            {
                'user_id': str(user.user_id),
                'user_name': user.user_name
            }
            for user in users_query
        ]


class UserResource(Resource):
    def __init__(self, **kwargs):
        self._db_instance = kwargs['db']

    def get(self, user_id):
        user_alias = aliased(Users)
        user = self._db_instance.session.query(
            user_alias
        ).filter_by(user_id=user_id).first()

        if not user:
            return {"message": f"user with user_id: {user_id} not found"}, 404
        else:
            return {
                'user_id': str(user.user_id),
                'user_name': str(user.user_name)
            }
