from raiden_client.plugins.v1.address import AddressPlugin


def test_address() -> None:
    address = AddressPlugin()
    assert address.endpoint == "/address"
    assert address.method == "get"
    assert not address.payload()
