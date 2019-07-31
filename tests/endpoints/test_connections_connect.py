from raiden_client.endpoints.connections_connect import (
    ConnectionConnectRequest,
    ConnectionConnectResponse,
)
from raiden_client.types import Address


def test_connection_connect_simple_request():
    connection = ConnectionConnectRequest(token_address=Address("0x123"), funds=100)
    assert connection.endpoint == f"/connections/{connection.token_address}"
    assert connection.method == "put"
    assert "funds" in connection.payload()
    assert "initial_channel_target" not in connection.payload()
    assert "joinable_funds_target" not in connection.payload()


def test_connection_initial_channel_target():
    connection = ConnectionConnectRequest(token_address=Address("0x123"), funds=100, initial_channel_target=10)
    assert connection.endpoint == f"/connections/{connection.token_address}"
    assert connection.method == "put"
    assert "funds" in connection.payload()
    assert "initial_channel_target" in connection.payload()
    assert "joinable_funds_target" not in connection.payload()


def test_connection_joinable_funds_target():
    connection = ConnectionConnectRequest(token_address=Address("0x123"), funds=100, joinable_funds_target=10)
    assert connection.endpoint == f"/connections/{connection.token_address}"
    assert connection.method == "put"
    assert "funds" in connection.payload()
    assert "initial_channel_target" not in connection.payload()
    assert "joinable_funds_target" in connection.payload()
