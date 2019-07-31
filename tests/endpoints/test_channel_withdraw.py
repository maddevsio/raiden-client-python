from raiden_client.endpoints.channel_withdraw import ChannelWithdrawRequest
from raiden_client.types import Address


def test_channel_withdraw_request():
    request = ChannelWithdrawRequest(
        token_address=Address("0x123"), partner_address=Address("0x321"), total_withdraw=200
    )
    assert request.endpoint == f"/channels/{request.token_address}/{request.partner_address}"
    assert request.method == "patch"

    payload = request.payload()
    assert "total_withdraw" in payload
    assert payload["total_withdraw"] == 200
