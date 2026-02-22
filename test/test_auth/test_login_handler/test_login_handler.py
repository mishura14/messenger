from collections import UserList
from unittest.mock import MagicMock, patch

import pytest
from redis.typing import ResponseT

from app.handler.login_handler.login_handler import LoginHandler
from app.model.model import UserLogin

test_user = UserLogin(email="misuraaleksej60@gmail.com", password="Mishura_14")


# тест успешный вход
@patch("app.handler.login_handler.login_handler.insert_refresh_token")
@patch("app.handler.login_handler.login_handler.create_access_token")
@patch("app.handler.login_handler.login_handler.create_refresh_token")
@patch("app.handler.login_handler.login_handler.check_hash")
@patch("app.handler.login_handler.login_handler.get_user_by_email")
@patch("app.handler.login_handler.login_handler.hash")
def test_login_success(
    mock_hash,
    mock_get_user_by_email,
    mock_check_hash,
    mock_create_refresh_token,
    mock_create_access_token,
    mock_insert_refresh_token,
):
    mock_get_user_by_email.return_value = {"id": 1, "password": "hashed_password"}
    mock_check_hash.return_value = True
    mock_create_refresh_token.return_value = "refresh_token"
    mock_create_access_token.return_value = "access_token"
    mock_hash.return_value = "refresh_token"

    response = LoginHandler(test_user)

    assert response["refresh"] == "refresh_token"
    assert response["access"] == "access_token"
    mock_insert_refresh_token.assert_called_once_with(1, "refresh_token")


# тест: пользователь не найден
@patch("app.handler.login_handler.login_handler.get_user_by_email")
def test_user_not_found(mock_get_user):
    mock_get_user.return_value = None
    response = LoginHandler(test_user)
    assert response == {"error": "User not found"}


# тест: неверный пароль
@patch("app.handler.login_handler.login_handler.get_user_by_email")
@patch("app.handler.login_handler.login_handler.check_hash")
def test_invalid_password(mock_check_hash, mock_get_user):
    mock_get_user.return_value = {"id": 1, "password": "hashed_password"}
    mock_check_hash.return_value = False

    response = LoginHandler(test_user)

    assert response == {"error": "Invalid password"}


# ошибка создания refresh token
@patch("app.handler.login_handler.login_handler.get_user_by_email")
@patch("app.handler.login_handler.login_handler.check_hash")
@patch("app.handler.login_handler.login_handler.create_refresh_token")
def test_failed_refresh_token(
    mock_create_refresh, mock_check_hash, mock_get_user_by_email
):
    mock_get_user_by_email.return_value = {"id": 1, "password": "hashed_password"}
    mock_check_hash.return_value = True
    mock_create_refresh.return_value = None
    response = LoginHandler(test_user)
    assert response == {"error": "Failed to create refresh token"}


# ошибка создания refresh token
@patch("app.handler.login_handler.login_handler.get_user_by_email")
@patch("app.handler.login_handler.login_handler.check_hash")
@patch("app.handler.login_handler.login_handler.create_refresh_token")
@patch("app.handler.login_handler.login_handler.create_access_token")
def test_failed_access_token(
    mock_create_access, mock_create_refresh, mock_check_hash, mock_get_user_by_email
):
    mock_get_user_by_email.return_value = {"id": 1, "password": "hashed_password"}
    mock_check_hash.return_value = True
    mock_create_refresh.return_value = "refresh_token"
    mock_create_access.return_value = None

    response = LoginHandler(test_user)
    assert response == {"error": "Failed to create access token"}
