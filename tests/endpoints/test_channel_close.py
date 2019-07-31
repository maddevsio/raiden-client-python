from raidenpy.endpoints.channel_close import ChannelCloseRequest
from raidenpy.types import Address


def test_channel_close_request():
    request = ChannelCloseRequest(
        token_address=Address("0x123"),
        partner_address=Address("0x321"),
    )
    assert request.endpoint == f"/channels/{request.token_address}/{request.partner_address}"
    assert request.method == "patch"

    payload = request.payload()
    assert "state" in payload
    assert payload["state"] == "closed"
