from flask_restful import Resource
from sqlalchemy.orm import Session
from ..repository.user_repository import UserRepository


class UserListResource(Resource):
    def __init__(self, **kwargs):
        self._db_instance = kwargs['db']

    def get(self):
        session: Session = self._db_instance.session
        with session.begin():
            user_repository = UserRepository(session)
            users_query = user_repository.get_list()

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
        session: Session = self._db_instance.session
        with session.begin():
            user_repository = UserRepository(session)
            user = user_repository.get(user_id)

            if not user:
                return {"message": f"user with user_id: {user_id} not found"}, 404
            else:
                return {
                    'user_id': str(user.user_id),
                    'user_name': str(user.user_name)
                }
