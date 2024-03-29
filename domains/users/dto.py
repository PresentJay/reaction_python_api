from pydantic import BaseModel
from typing import Optional


class UserItemGetResponse(BaseModel):
    class DTO(BaseModel):
        id: int
        name: str
        flavor_genre_first: Optional[str]
        flavor_genre_second: Optional[str]
        flavor_genre_third: Optional[str]
        created_at: str
        updated_at: str

    data: DTO


class UserPostRequest(BaseModel):
    user_name: str
    user_password: str


class UserPostResponse(BaseModel):
    id: int
