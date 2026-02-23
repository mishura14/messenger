from unittest.mock import patch

import pytest
from fastapi.exceptions import HTTPException

from app.handler.refresh_token.refresj_token import refresh_update_token
from app.model.model import RefreshUpdate

# тестовые данные
test_refresh_token = RefreshUpdate(refresh_token="fake_refresh_token")


def test_refresh_update_token_success():
    with (
        patch(
            "app.handler.refresh_token.refresj_token.decoder_refresh_token"
        ) as mock_decoder,
        patch(
            "app.handler.refresh_token.refresj_token.get_refresh_token"
        ) as mock_get_refresh,
        patch("app.handler.refresh_token.refresj_token.check_hash") as mock_check_hash,
        patch(
            "app.handler.refresh_token.refresj_token.create_access_token"
        ) as mock_create_access,
        patch(
            "app.handler.refresh_token.refresj_token.create_refresh_token"
        ) as mock_create_refresh,
        patch(
            "app.handler.refresh_token.refresj_token.update_refresh_token"
        ) as mock_update_refresh,
        patch("app.handler.refresh_token.refresj_token.hash") as mock_hash,
    ):
        mock_decoder.return_value = 1
        mock_get_refresh.return_value = {"hash_refresh_token": "hashed_refresh"}
        mock_check_hash.return_value = True
        mock_create_access.return_value = "new_access_token"
        mock_create_refresh.return_value = "new_refresh_token"
        mock_hash.return_value = "hashed_new_refresh_token"

        result = refresh_update_token(test_refresh_token)

        assert result["access_token"] == "new_access_token"
        assert result["refresh_token"] == "new_refresh_token"

        mock_update_refresh.assert_called_once_with(1, "hashed_new_refresh_token")


def test_refresh_update_token_invalid_token():
    with patch(
        "app.handler.refresh_token.refresj_token.decoder_refresh_token"
    ) as mock_decoder:
        mock_decoder.return_value = None
        with pytest.raises(HTTPException) as exc_info:
            refresh_update_token(test_refresh_token)
        assert exc_info.value.status_code == 401
        assert "Invalid refresh token" in exc_info.value.detail


def test_refresh_update_token_hash_mismatch():
    with (
        patch(
            "app.handler.refresh_token.refresj_token.decoder_refresh_token"
        ) as mock_decoder,
        patch(
            "app.handler.refresh_token.refresj_token.get_refresh_token"
        ) as mock_get_refresh,
        patch("app.handler.refresh_token.refresj_token.check_hash") as mock_check_hash,
    ):
        mock_decoder.return_value = 1
        mock_get_refresh.return_value = {"hash_refresh_token": "hashed_refresh"}
        mock_check_hash.return_value = False

        with pytest.raises(HTTPException) as exc_info:
            refresh_update_token(test_refresh_token)
        assert exc_info.value.status_code == 401
        assert "Invalid time refresh token" in exc_info.value.detail
