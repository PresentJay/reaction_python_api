from fastapi import APIRouter, Depends
from dependencies.database import provide_session

name = "Users"
router = APIRouter()


@router.post(f"/{name}/login")
async def login(
    payload=any,
    db=Depends(provide_session),
):
    pass


@router.post(f"/{name}/logout")
async def logout(
    payload=any,
    db=Depends(provide_session),
):
    pass


@router.post(f"/{name}/checkid")
async def checkid(
    payload=any,
    db=Depends(provide_session),
):
    pass


@router.post(f"/{name}/delete")
async def delete(
    payload=any,
    db=Depends(provide_session),
):
    pass


@router.post(f"/{name}/create")
async def create(
    payload=any,
    db=Depends(provide_session),
):
    pass


@router.get(f"/{name}/{{user_id}}")
async def get(
    user_id,
    db=Depends(provide_session),
):
    pass
