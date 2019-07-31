from raidenpy.endpoints.connections import ConnectionsRequest, ConnectionsResponse


def test_connection_request():
    connection = ConnectionsRequest()
    assert connection.endpoint == "/connections"
    assert connection.method == "get"
    assert not connection.payload()


def test_connection_response():
    connection = ConnectionsResponse.from_dict({
        "connections": {}
    })
    assert "connections" in connection.to_dict()