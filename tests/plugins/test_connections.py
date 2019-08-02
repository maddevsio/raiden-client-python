from raiden_client.plugins.v1.connections import ConnectionsPlugin


def test_connection_request():
    connection = ConnectionsPlugin()
    assert connection.endpoint == "/connections"
    assert connection.method == "get"
    assert not connection.payload()
