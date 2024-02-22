from domains import Service

from dependencies.auth import hash_password
from .repositories import UserRepository
from .models import UserModel


class UserService(Service):
    def __init__(
        self,
        *,
        user_repository: UserRepository,
    ):
        self._user_repository = user_repository

    def get_user(self, *, user_id: int) -> UserModel:
        user_entity = self._user_repository.get_user(user_id=user_id)
        return user_entity

    def create_user(self, *, user_name, user_pw) -> int:
        hashed_pw = hash_password(user_pw)

        user_entity = self._user_repository.create_user(
            user_name=user_name,
            password=hashed_pw,
        )
        return user_entity

    def get_user_by_name(self, *, user_name: str) -> UserModel:
        user_entity = self._user_repository.get_user_by_name(
            user_name=user_name,
        )
        return user_entity
