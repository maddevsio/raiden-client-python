from raidenpy.types import Address
from raidenpy.endpoints.channels import ChannelsRequest, ChannelsResponse


def test_channel_all():
    channels = ChannelsRequest()
    assert channels.endpoint == "/channels"
    assert channels.method == "get"
    assert not channels.payload()


def test_channel_by_token_address():
    channels = ChannelsRequest(token_address=Address("0x123"))
    assert channels.endpoint == "/channels/0x123"
    assert channels.method == "get"
    assert not channels.payload()


def test_channel_response():
    response = ChannelsResponse.from_dict({"channels": []})
    assert "channels" in response.to_dict()
