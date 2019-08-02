from raiden_client.plugins.v1 import AddressPlugin


def test_plugin() -> None:
    address = AddressPlugin()
    assert address.name == "address"
    assert address.endpoint == "/address"
    assert address.method == "get"
    assert address.version == "v1"
