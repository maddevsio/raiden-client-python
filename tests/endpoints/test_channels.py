from raiden_client.endpoints.channels import Channels


def test_channels_all() -> None:
    channels = Channels()
    assert channels.endpoint == "/channels"
    assert channels.method == "get"
    assert channels.name == "channels"
    assert not channels.payload()


def test_channels_by_token_address() -> None:
    channels = Channels(token_address="0x145737846791E749f96344135Ce211BE8C510a17")
    assert channels.endpoint == f"/channels/{channels.token_address}"
    assert channels.method == "get"
    assert not channels.payload()
