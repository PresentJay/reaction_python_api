from sqlalchemy import Column, DateTime, String, Integer, func


from dependencies.database import Base


class UserModel(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    flavor_genre_first = Column(String)
    flavor_genre_second = Column(String)
    flavor_genre_third = Column(String)
    created_at = Column(DateTime, server_default=func.utc_timestamp())
    updated_at = Column(
        DateTime,
        server_default=func.utc_timestamp(),
        server_onupdate=func.utc_timestamp(),
    )
