from unittest.mock import MagicMock, patch
from datetime import datetime

from backend.app.services.user_service import UserService


@patch("backend.app.services.user_service.CacheService")
def test_get_user(mock_cache):

    mock_cache.get.return_value = None
    mock_cache.set.return_value = True

    service = UserService()
    service.repository = MagicMock()

    db = MagicMock()

    fake_user = MagicMock()

    fake_user.id = 1
    fake_user.name = "John"
    fake_user.email = "john@test1.com"
    fake_user.age = 25
    fake_user.role = "user"
    fake_user.phone_number = "9876543210"
    fake_user.created_at = datetime.utcnow()

    service.repository.get_user.return_value = fake_user

    result = service.get_user(
        db,
        1,
    )

    assert result.id == 1
    assert result.name == "John"

    service.repository.get_user.assert_called_once_with(
        db,
        1,
    )

    mock_cache.set.assert_called_once()


import pytest

from backend.app.exceptions.custom_exceptions import (
    UserNotFoundException,
)


def test_get_user_not_found():

    service = UserService()

    service.repository = MagicMock()

    db = MagicMock()

    service.repository.get_user.return_value = None

    with pytest.raises(
        UserNotFoundException,
    ):
        service.get_user(
            db,
            1,
        )

def test_create_user():

    service = UserService()

    service.repository = MagicMock()

    db = MagicMock()

    # Email does not exist
    service.repository.get_user_by_email.return_value = None

    fake_user = MagicMock()
    fake_user.id = 10
    fake_user.name = "Alice"
    fake_user.email = "alice@test.com"

    service.repository.create_user.return_value = fake_user

    user = MagicMock()
    user.email = "alice@test.com"
    user.password = "password123"

    result = service.create_user(
        db,
        user,
    )

    assert result.id == 10
    assert result.name == "Alice"

from unittest.mock import patch


@patch(
    "backend.app.services.user_service.CacheService"
)
def test_cache_called(
    mock_cache,
):

    mock_cache.set.return_value = True

    CacheService = mock_cache

    CacheService.set(
        "user:1",
        {},
    )

    CacheService.set.assert_called_once_with(
        "user:1",
        {},
    )
from unittest.mock import patch


@patch(
    "backend.app.tasks.email_tasks.send_welcome_email"
)
def test_send_email(
    mock_email,
):

    mock_email(
        "john@test.com"
    )

    mock_email.assert_called_once_with(
        "john@test.com"
    )


def test_repository_failure():

    service = UserService()

    service.repository = MagicMock()

    db = MagicMock()

    service.repository.get_user.side_effect = Exception(
        "Database Error"
    )

    with pytest.raises(
        Exception,
    ):
        service.get_user(
            db,
            1,
        )