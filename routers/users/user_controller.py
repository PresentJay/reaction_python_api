import arrow
from fastapi import APIRouter, Depends, HTTPException, status, Form

from dependencies.database import provide_session
from dependencies.auth import (
    Token,
    verify_password,
    create_access_token,
)
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
async def get_item(
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
            created_at=str(arrow.get(user.created_at)),
            updated_at=str(arrow.get(user.updated_at)),
        )
    )


@router.post(f"/{name}/login")
async def login(
    user_name: str = Form(...),
    user_password: str = Form(...),
    db=Depends(provide_session),
) -> Token:
    user_service = UserService(user_repository=UserRepository(session=db))
    user = user_service.get_user_by_name(user_name=user_name)

    if not verify_password(user_password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="비밀번호가 틀립니다.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user.id})
    return Token(token=access_token, type="bearer")
