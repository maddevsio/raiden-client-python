from raiden_client.endpoints.connection_disconnect import (
    ConnectionDisconnectRequest,
)
from raiden_client.types import Address


def test_connection_connect_simple_request():
    connection = ConnectionDisconnectRequest(token_address=Address("0x123"))
    assert connection.endpoint == f"/connections/{connection.token_address}"
    assert connection.method == "delete"
    assert not connection.payload()
