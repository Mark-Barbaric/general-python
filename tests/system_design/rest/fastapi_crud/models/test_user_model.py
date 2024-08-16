from src.system_design.rest.fastapi_crud.app.model import UserModel
from uuid import uuid4
from pydantic import ValidationError, SecretStr
import pytest


def test_valid_user_model():
    user_model = UserModel(user_id=uuid4(),
                           user_name="markbarbaric",
                           password="password",
                           password_bytes=b"password_bytes",
                           email="mark@hotmail.com")
    assert isinstance(user_model.user_name, str)
    assert isinstance(user_model.email, str)


def test_password_input():
    user_model = UserModel(user_id=uuid4(),
                           user_name="markbarbaric",
                           password="password",
                           password_bytes=b"password_bytes",
                           email="mark@hotmail.com")
    assert isinstance(user_model.password, SecretStr)


def test_immutable_user_id():
    user_model = UserModel(user_id=uuid4(),
                           user_name="markbarbaric",
                           password="password",
                           password_bytes=b"password_bytes",
                           email="mark@hotmail.com")

    with pytest.raises(ValidationError) as exc:
        user_model.user_id = uuid4()

    validation_errors = exc.value.errors()
    assert len(validation_errors) == 1
    assert validation_errors[0]['type'] == 'frozen_field'


def test_invalid_user_model():
    with pytest.raises(ValidationError) as exc:
        user_model = UserModel(user_id=uuid4(),  # noqa: F841
                               user_name="markbarbaric",
                               email="mark@hotmail.com",
                               password="password",
                               password_bytes=b"password_bytes",
                               description="not valid")

    validation_errors = exc.value.errors()
    assert len(validation_errors) == 1
    error_type = validation_errors[0]['type']
    assert error_type == 'extra_forbidden'


def test_invalid_user_name():
    with pytest.raises(ValidationError) as exc:
        user_model = UserModel(user_id=uuid4(),  # noqa: F841
                               email="mark@gotmail.com",
                               password="password",
                               password_bytes=b"password_bytes",
                               user_name='ma')

    validation_errors = exc.value.errors()
    assert len(validation_errors) == 1
    error_type = validation_errors[0]['type']
    assert error_type == 'string_too_short'
