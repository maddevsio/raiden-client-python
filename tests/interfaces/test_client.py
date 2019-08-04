from unittest import mock

import requests

from raiden_client import Client


client = Client()


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

    def json():
        return {"our_address": "0x123"}

    mockresponse.json = json

    address = client.address()
    assert "our_address" in address
    assert address["our_address"] == "0x123"


@mock.patch.object(requests, 'request')
def test_client_tokens(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return ["0x123", "0x456"]

    mockresponse.json = json

    tokens = client.tokens()
    assert "tokens" in tokens
    assert len(tokens["tokens"]) > 0


@mock.patch.object(requests, 'request')
def test_client_tokens_filtered(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return ["0x123", "0x456"]

    mockresponse.json = json

    tokens = client.tokens(token_address="0x145737846791E749f96344135Ce211BE8C510a17")
    assert "tokens" in tokens
    assert len(tokens["tokens"]) > 0


@mock.patch.object(requests, 'request')
def test_client_non_settled_partners(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {
            "non_settled_partners": "0x145737846791E749f96344135Ce211BE8C510a17",
        }

    mockresponse.json = json

    tokens = client.non_settled_partners(token_address="0x145737846791E749f96344135Ce211BE8C510a17")
    assert "non_settled_partners" in tokens
    assert len(tokens["non_settled_partners"]) > 0
