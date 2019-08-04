import pytest

from raiden_client.exceptions import ResponseStatusCodeException
from raiden_client.raiden_api import RaidenAPI


raiden_api = RaidenAPI(endpoint="http://127.0.0.1:5001", version="v1")


def test_raiden_api_url() -> None:
    expected_url = f"http://127.0.0.1:5001/api/v1/address"
    assert raiden_api.url("/address") == expected_url


def test_raiden_validate_status_code() -> None:
    assert raiden_api.validate_status_code(200, "ok") == 200
    assert raiden_api.validate_status_code(201, "ok") == 201


def test_raiden_status_code_fail() -> None:
    with pytest.raises(ResponseStatusCodeException):
        assert raiden_api.validate_status_code(404, "ok")
