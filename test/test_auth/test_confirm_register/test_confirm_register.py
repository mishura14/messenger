from pickletools import pybytes, pybytes_or_str
from unittest.mock import patch

import pytest
from fastapi import HTTPException

from app.handler.confirm_register_handler.confirm_register_hendler import (
    confirm_register,
)
from app.model.model import CodeRegister


# успешное подтвержедние регистрации
@patch("app.handler.confirm_register_handler.confirm_register_hendler.rd")
@patch("app.handler.confirm_register_handler.confirm_register_hendler.register_user")
@patch(
    "app.handler.confirm_register_handler.confirm_register_hendler.get_verification_data"
)
def test_confirm_register(
    mock_get_verification_data,
    mock_register_user,
    mock_rd,
):
    mock_get_verification_data.return_value = {
        "name": "Mishura",
        "email": "misuraaleksej60@gmail.com",
        "password": "hashed_pass",
    }

    code = CodeRegister(code="123456")
    result = confirm_register(code)

    assert result == {"message": "регистрация подтверждена"}

    mock_get_verification_data.assert_called_once_with(mock_rd, "123456")
    mock_register_user.assert_called_once_with(
        "Mishura",
        "misuraaleksej60@gmail.com",
        "hashed_pass",
    )
    mock_rd.delete.assert_called_once_with("verify:123456")


# тест ошибка не найденного кода


@patch(
    "app.handler.confirm_register_handler.confirm_register_hendler.get_verification_data"
)
@patch("app.handler.confirm_register_handler.confirm_register_hendler.register_user")
@patch("app.handler.confirm_register_handler.confirm_register_hendler.rd")
def test_confirm_register_invalid_code(
    mock_rd, mock_register_user, mock_get_verification
):
    # Код не найден
    mock_get_verification.return_value = None

    code = CodeRegister(code="000000")

    # Проверяем, что вызывается HTTPException
    with pytest.raises(HTTPException) as exc_info:
        confirm_register(code)
    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Неверный или просроченный код подтверждения"

    # register_user и rd.delete не должны вызываться
    mock_register_user.assert_not_called()
    mock_rd.delete.assert_not_called()
