from raiden_client.endpoints.channel_deposit import ChannelDepositRequest
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
