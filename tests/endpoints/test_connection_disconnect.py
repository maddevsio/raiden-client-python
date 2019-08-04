from raiden_client.endpoints.connection_disconnect import Disconnect


def test_connection_disconnect_simple_request() -> None:
    connection = Disconnect(token_address="0x145737846791E749f96344135Ce211BE8C510a17")
    assert connection.endpoint == f"/connections/{connection.token_address}"
    assert connection.method == "delete"
    assert connection.name == "disconnect"
    assert not connection.payload()
