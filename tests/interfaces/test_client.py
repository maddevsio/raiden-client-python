from unittest import mock

import requests

from raiden_client import Client


client = Client()


def test_is_disconnected() -> None:
    assert not client.is_connected


@mock.patch.object(requests, 'request')
def test_client_is_connected(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"
    mockresponse.return_value = {"our_address": "0x123"}
    assert client.is_connected


@mock.patch.object(requests, 'request')
def test_client_address(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"
    mockresponse.return_value = {"our_address": "0x123"}

    address = client.address()
    assert "our_address" in address
