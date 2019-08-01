from raiden_client.endpoints.channel_deposit import ChannelDepositRequest, ChannelDepositResponse
from raiden_client.types import Address


def test_channel_deposit_request():
    request = ChannelDepositRequest(
        token_address=Address("0x123"), partner_address=Address("0x321"), total_deposit=2000
    )
    assert request.endpoint == f"/channels/{request.token_address}/{request.partner_address}"
    assert request.method == "patch"

    payload = request.payload()
    assert "total_deposit" in payload
    assert payload["total_deposit"] == 2000


def test_channel_deposit_response():
    response = ChannelDepositResponse.from_dict({
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
