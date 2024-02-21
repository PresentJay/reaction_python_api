from fastapi import APIRouter, Depends
from dependencies.database import provide_session
from domains.users.services import UserService
from domains.users.repositories import UserRepository
from domains.users.dto import (
    UserItemGetResponse,
    UserPostRequest,
    UserPostResponse,
)

name = "users"
router = APIRouter()


@router.post(f"/{name}/create")
async def create(
    payload: UserPostRequest,
    db=Depends(provide_session),
) -> UserPostResponse:
    user_service = UserService(user_repository=UserRepository(session=db))

    user = user_service.create_user(
        user_name=payload.user_name,
        user_pw=payload.user_password,
    )

    return UserPostResponse(id=user.id)


@router.get(f"/{name}/{{user_id}}")
async def get(
    user_id,
    db=Depends(provide_session),
) -> UserItemGetResponse:
    user_service = UserService(user_repository=UserRepository(session=db))

    user = user_service.get_user(user_id=user_id)

    return UserItemGetResponse(
        data=UserItemGetResponse.DTO(
            id=user.id,
            name=user.name,
            flavor_genre_first=user.flavor_genre_first,
            flavor_genre_second=user.flavor_genre_second,
            flavor_genre_third=user.flavor_genre_third,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )
    )
