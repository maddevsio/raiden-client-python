from raiden_client.endpoints.connections_connect import Connect


def test_connection_connect_simple_request() -> None:
    connection = Connect(token_address="0x145737846791E749f96344135Ce211BE8C510a17", funds=100)
    assert connection.endpoint == f"/connections/{connection.token_address}"
    assert connection.method == "put"
    assert connection.name == "connect"
    assert "funds" in connection.payload()
    assert "initial_channel_target" not in connection.payload()
    assert "joinable_funds_target" not in connection.payload()


def test_connection_initial_channel_target() -> None:
    connection = Connect(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        funds=100,
        initial_channel_target=10,
    )
    assert connection.endpoint == f"/connections/{connection.token_address}"
    assert "funds" in connection.payload()
    assert "initial_channel_target" in connection.payload()
    assert "joinable_funds_target" not in connection.payload()


def test_connection_joinable_funds_target() -> None:
    connection = Connect(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17", funds=100, joinable_funds_target=10
    )
    assert connection.endpoint == f"/connections/{connection.token_address}"
    assert "funds" in connection.payload()
    assert "initial_channel_target" not in connection.payload()
    assert "joinable_funds_target" in connection.payload()


def test_connect_to_dict() -> None:
    connection = Connect(token_address="0x145737846791E749f96344135Ce211BE8C510a17", funds=100)
    connection.from_dict({
        "funds": 1,
        "sum_deposits": 2,
        "channels": 3,
    })
    data = connection.to_dict()
    assert "connection" in data
    assert "funds" in data["connection"]
    assert "sum_deposits" in data["connection"]
    assert "channels" in data["connection"]
