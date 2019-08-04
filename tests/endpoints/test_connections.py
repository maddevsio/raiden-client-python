from raiden_client.endpoints.connections import Connections


def test_connections_request():
    connection = Connections()
    assert connection.endpoint == "/connections"
    assert connection.method == "get"
    assert connection.name == "connections"
    assert not connection.payload()
