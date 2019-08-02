from raiden_client.plugins.v1.connection_disconnect import DisconnectPlugin


def test_connection_connect_simple_request():
    connection = DisconnectPlugin(token_address="0x145737846791E749f96344135Ce211BE8C510a17")
    assert connection.endpoint == f"/connections/{connection.token_address}"
    assert connection.method == "delete"
    assert not connection.payload()
