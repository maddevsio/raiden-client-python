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


@mock.patch.object(requests, 'request')
def test_client_channels(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"channels": []}

    mockresponse.json = json
    channels = client.channels()
    assert "channels" in channels


@mock.patch.object(requests, 'request')
def test_client_channels_token(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"channels": []}

    mockresponse.json = json
    channels = client.channels(token_address="0x145737846791E749f96344135Ce211BE8C510a17")
    assert "channels" in channels


@mock.patch.object(requests, 'request')
def test_client_channel(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"channel": {}}

    mockresponse.json = json
    channel = client.channel(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0x145737846791E749f96344135Ce211BE8C510a18",
    )
    assert "channel" in channel


@mock.patch.object(requests, 'request')
def test_client_pending_transfers(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"pending_transfers": {}}

    mockresponse.json = json
    pending_transfers = client.pending_transfers(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0x145737846791E749f96344135Ce211BE8C510a18",
    )
    assert "pending_transfers" in pending_transfers


@mock.patch.object(requests, 'request')
def test_client_token_register(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"token_network_address": {}}

    mockresponse.json = json
    token_network_address = client.token_register(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
    )
    assert "token_network_address" in token_network_address


@mock.patch.object(requests, 'request')
def test_client_channel_open(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"channel": {}}

    mockresponse.json = json
    channel = client.channel_open(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0x145737846791E749f96344135Ce211BE8C510a18",
        settle_timeout=100,
        total_deposit=3000,
    )
    assert "channel" in channel


@mock.patch.object(requests, 'request')
def test_client_channel_close(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"channel": {}}

    mockresponse.json = json
    channel = client.channel_close(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0x145737846791E749f96344135Ce211BE8C510a18",
    )
    assert "channel" in channel


@mock.patch.object(requests, 'request')
def test_client_increase_deposit(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"channel": {}}

    mockresponse.json = json
    channel = client.channel_increase_deposit(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0x145737846791E749f96344135Ce211BE8C510a18",
        total_deposit=3400,
    )
    assert "channel" in channel


@mock.patch.object(requests, 'request')
def test_client_increase_withdraw(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"channel": {}}

    mockresponse.json = json
    channel = client.channel_increase_withdraw(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0x145737846791E749f96344135Ce211BE8C510a18",
        total_withdraw=3400,
    )
    assert "channel" in channel


@mock.patch.object(requests, 'request')
def test_client_connections(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"connections": {}}

    mockresponse.json = json
    connections = client.connections()
    assert "connections" in connections


@mock.patch.object(requests, 'request')
def test_client_connections_connect(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"connection": {}}

    mockresponse.json = json
    connection = client.connections_connect(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        funds=100,
        initial_channel_target=10,
        joinable_funds_target=20,
    )
    assert "connection" in connection


@mock.patch.object(requests, 'request')
def test_client_connections_disconnect(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"connection": {}}

    mockresponse.json = json
    connection = client.connection_disconnect(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
    )
    assert "connection" in connection


@mock.patch.object(requests, 'request')
def test_client_payment(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"payment": {}}

    mockresponse.json = json
    payment = client.payment(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        target_address="0x145737846791E749f96344135Ce211BE8C510a18",
        amount=20,
        identifier=1,
    )
    assert "payment" in payment


@mock.patch.object(requests, 'request')
def test_client_payment_events(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"payment_events": {}}

    mockresponse.json = json
    payment_events = client.payment_events(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        target_address="0x145737846791E749f96344135Ce211BE8C510a18",
    )
    assert "payment_events" in payment_events


@mock.patch.object(requests, 'request')
def test_client_mint_tokens(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"mint_tokens": {}}

    mockresponse.json = json
    transaction_hash = client.mint_tokens(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        to="0x145737846791E749f96344135Ce211BE8C510a18",
        value=100,
        contract_method="mint",
    )
    assert "transaction_hash" in transaction_hash
