from raiden_client.endpoints.channel_close import ChannelCloseRequest, ChannelCloseResponse
from raiden_client.types import Address


def test_channel_close_request():
    request = ChannelCloseRequest(token_address=Address("0x123"), partner_address=Address("0x321"))
    assert request.endpoint == f"/channels/{request.token_address}/{request.partner_address}"
    assert request.method == "patch"

    payload = request.payload()
    assert "state" in payload
    assert payload["state"] == "closed"


def test_channel_close_response():
    response = ChannelCloseResponse.from_dict({
        "channel": {
            "token_network_address": Address("0x123"),
            "channel_identifier": int,
            "partner_address": Address("0x321"),
            "token_address": Address("0x3456"),
            "balance": 100,
            "total_deposit": 20,
            "total_withdraw": 10,
            "state": "opened",
            "settle_timeout": 100,
            "reveal_timeout": 200,
        }
    })
    assert "channel" in response.to_dict()
    channel = response.to_dict()
    assert "token_network_address" in channel["channel"]
