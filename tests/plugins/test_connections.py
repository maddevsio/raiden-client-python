from raiden_client.endpoints.v1.connections import Connections


def test_connection_request():
    connection = Connections()
    assert connection.endpoint == "/connections"
    assert connection.method == "get"
    assert not connection.payload()
