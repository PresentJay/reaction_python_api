from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from .models import UserModel


class UserRepository:
    def __init__(self, session: Session):
        self._session = session

    def get_user(self, *, user_id: int):
        user_entity = (
            self._session.query(UserModel)
            .filter(
                UserModel.id == user_id,
            )
            .first()
        )

        if user_entity is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="유저 정보가 없습니다.",
            )

        return user_entity

    def create_user(self, *, user_name: str, password: str):
        user_entity = UserModel(
            name=user_name,
            password=password,
        )

        try:
            self._session.add(user_entity)
            self._session.commit()
        except Exception as e:
            if isinstance(e, IntegrityError):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="입력한 name이 이미 있습니다.",
                )

        return user_entity

    def get_user_by_name(self, *, user_name):
        user_entity = (
            self._session.query(UserModel)
            .filter(
                UserModel.name == user_name,
            )
            .first()
        )

        if user_entity is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="유저 정보가 없습니다.",
            )

        return user_entity
