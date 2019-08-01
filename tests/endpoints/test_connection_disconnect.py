from raiden_client.endpoints.connection_disconnect import (
    ConnectionDisconnectRequest,
    ConnectionDisconnectResponse,
)
from raiden_client.types import Address


def test_connection_connect_simple_request():
    connection = ConnectionDisconnectRequest(token_address=Address("0x123"))
    assert connection.endpoint == f"/connections/{connection.token_address}"
    assert connection.method == "delete"
    assert not connection.payload()


def test_connection_disconnect_response():
    response = ConnectionDisconnectResponse.from_dict({
        "connection": {
            Address("0x123123"): {
                "funds": 123,
                "sum_deposits": 100,
                "channels": 1,
            }
        }
    })
    assert "connection" in response.to_dict()
