from sqlalchemy.orm import Session, aliased
from .abstract_repository import AbstractRepository
from ..domain.users import Users


class UserRepository(AbstractRepository):
    def __init__(self, session):
        self._session: Session = session

    def get(self, user_id) -> Users | None:
        user_alias = aliased(Users)
        user = self._session.query(
            user_alias
        ).filter_by(user_id=user_id).first()
        return user

    def get_list(self) -> list[Users]:
        return self._session.query(Users).all()

    def add(self) -> None:
        raise NotImplementedError
