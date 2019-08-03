from raiden_client.endpoints.v1.channels import Channels


def test_channel_all() -> None:
    channels = Channels()
    assert channels.endpoint == "/channels"
    assert channels.method == "get"
    assert not channels.payload()


def test_channel_by_token_address() -> None:
    channels = Channels(token_address="0x145737846791E749f96344135Ce211BE8C510a17")
    assert channels.endpoint == f"/channels/{channels.token_address}"
    assert channels.method == "get"
    assert not channels.payload()
