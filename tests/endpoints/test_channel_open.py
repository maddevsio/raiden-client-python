from raidenpy.endpoints.channel_open import (
    ChannelOpenRequest,
    ChannelOpenResponse,
)
from raidenpy.types import Address


def test_channel_open_request():
    request = ChannelOpenRequest(
        token_address=Address("0x123"), partner_address=Address("0x321"), total_deposit=35000000, settle_timeout=500
    )
    assert request.endpoint == "/channels"
    assert request.method == "put"
    assert "token_address" in request.payload()
    assert "partner_address" in request.payload()
    assert "total_deposit" in request.payload()
    assert "settle_timeout" in request.payload()


def test_channel_open_response():
    channel = {
        "token_network_address": "0xE5637F0103794C7e05469A9964E4563089a5E6f2",
        "channel_identifier": 20,
        "partner_address": "0x61C808D82A3Ac53231750daDc13c777b59310bD9",
        "token_address": "0xEA674fdDe714fd979de3EdF0F56AA9716B898ec8",
        "balance": 25000000,
        "total_deposit": 35000000,
        "total_withdraw": 0,
        "state": "opened",
        "settle_timeout": 500,
        "reveal_timeout": 30,
    }
    response = ChannelOpenResponse(channel=channel)
    assert "channel" in response.to_dict()
    opened_channel_response = response.to_dict()

    opened_channel = opened_channel_response["channel"]
    assert "token_network_address" in opened_channel
    assert "channel_identifier" in opened_channel
    assert "partner_address" in opened_channel
    assert "token_address" in opened_channel
    assert "balance" in opened_channel
    assert "total_deposit" in opened_channel
    assert "total_withdraw" in opened_channel
    assert "state" in opened_channel
    assert "settle_timeout" in opened_channel
    assert "reveal_timeout" in opened_channel
