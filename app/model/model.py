import re

from pydantic import BaseModel, EmailStr, Field
from pydantic.functional_validators import field_validator
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


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
