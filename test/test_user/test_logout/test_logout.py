from unittest.mock import patch

from app.handler.logout_handler.logout_handler import logout


def test_logout():
    with patch(
        "app.handler.logout_handler.logout_handler.delete_refresh_token"
    ) as mock_delete:

        def fake_user_middleware():
            return 42

        response = logout(user_id=fake_user_middleware())

        mock_delete.assert_called_once_with(42)

        assert response == {"message": "Logged out successfully"}
