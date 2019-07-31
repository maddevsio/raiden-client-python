from raiden_client.endpoints.channel import ChannelRequest, ChannelResponse
from raiden_client.types import Address


def test_channel():
    channel = ChannelRequest(token_address=Address("0x123"), partner_address=Address("0x321"))
    assert channel.endpoint == "/channels/0x123/0x321"
    assert channel.method == "get"
    assert not channel.payload()


def test_channel_response():
    response = ChannelResponse.from_dict({"channel": {}})
    assert "channel" in response.to_dict()
