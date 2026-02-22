from unittest.mock import ANY, patch

from app.handler.register_handler.register_handler import RegisterHandler
from app.model.model import UserRegister


# ----------------------
# тест: пользователь уже существует
# ----------------------
@patch("app.handler.register_handler.register_handler.check_user_by_email")
def test_register_user_exists(mock_check_user_by_email):
    mock_check_user_by_email.return_value = True

    user = UserRegister(
        name="Mishura", email="misuraaleksej60@gmail.com", password="Mishura_14"
    )
    result = RegisterHandler(user)

    assert result == {"error": "user already exists"}
    mock_check_user_by_email.assert_called_once_with(user.email)


# тест: пользователь успешно зарегистрирован
@patch("app.handler.register_handler.register_handler.save_code_redis")
@patch("app.handler.register_handler.register_handler.send_verification_email")
@patch("app.handler.register_handler.register_handler.generate_verification_code")
@patch("app.handler.register_handler.register_handler.hash.hash")
@patch("app.handler.register_handler.register_handler.check_user_by_email")
def test_register(
    mock_check_user_by_email,
    mock_hash,
    mock_generate_verification_code,
    mock_send_verification_email,
    mock_save_code_redis,
):
    mock_check_user_by_email.return_value = False
    mock_hash.return_value = "hashed_pass"
    mock_generate_verification_code.return_value = "123456"

    user = UserRegister(
        name="mishura", email="misuraaleksej60@gmail.com", password="Mishura_14"
    )
    result = RegisterHandler(user)

    assert "message" in result
    assert result["message"].startswith("код регистрации")

    mock_check_user_by_email.assert_called_once_with(user.email)
    mock_hash.assert_called_once_with(user.password)
    mock_generate_verification_code.assert_called_once()
    mock_send_verification_email.assert_called_once()
    mock_save_code_redis.assert_called_once_with(
        ANY, user.name, user.email, "hashed_pass", "123456"
    )
