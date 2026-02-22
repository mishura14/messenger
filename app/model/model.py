import re
from datetime import datetime

from pydantic import BaseModel, EmailStr, Field
from pydantic.functional_validators import field_validator
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm.properties import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, DateTime


# класс UserRegister для регистрации пользователя
class UserRegister(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def validete_password(cls, value: str):
        if not (len(value) >= 8 and len(value) <= 30):
            raise ValueError("Invalid length password")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r"[!@#$%&*()_-]", value):
            raise ValueError("Password must contain at least one special character")
        return value


# class для полеченя данных пользователя с bd
class UserDb(BaseModel):
    id: int
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def validete_password(cls, value: str):
        if not (len(value) >= 8 and len(value) <= 30):
            raise ValueError("Invalid length password")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one digit")
        if not re.search(r"[!@#$%&*()_-]", value):
            raise ValueError("Password must contain at least one special character")
        return value


# class для кода регистрации
class CodeRegister(BaseModel):
    code: str = Field(min_length=6, max_length=6)


# создание таблиц для микраций
class Base(DeclarativeBase):
    pass


# создание таблицы пользователей
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password: Mapped[str] = mapped_column(String(255))


# таблица в бд для refresh token
class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    hash_refresh_token: Mapped[str] = mapped_column(String(255), nullable=False)
    expires_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    revoked: Mapped[bool] = mapped_column(Boolean, default=False)
