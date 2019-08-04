from unittest import mock

import pytest

from raiden_client.exceptions import ResponseStatusCodeException
from raiden_client.raiden_api import RaidenAPI
from raiden_client.endpoints.address import Address


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


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code, text):
            self.json_data = json_data
            self.status_code = status_code
            self.text = "ok"

        def json(self):
            return self.json_data

    response = {
        "our_address": "0x123"
    }
    return MockResponse(response, 200, "ok")


@mock.patch('requests.request', side_effect=mocked_requests_get)
def test_request_mocked(mock_get) -> None:
    endpoint = Address()
    response = raiden_api.request(endpoint)
    assert "our_address" in response
