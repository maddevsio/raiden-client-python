from raiden_client.plugins.v1.channels import ChannelsPlugin


def test_channel_all() -> None:
    channels = ChannelsPlugin()
    assert channels.endpoint == "/channels"
    assert channels.method == "get"
    assert not channels.payload()


def test_channel_by_token_address() -> None:
    channels = ChannelsPlugin(token_address="0x145737846791E749f96344135Ce211BE8C510a17")
    assert channels.endpoint == f"/channels/{channels.token_address}"
    assert channels.method == "get"
    assert not channels.payload()
