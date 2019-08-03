from raiden_client.endpoints.channel_close import ChannelClose


def test_channel_close_request() -> None:
    request = ChannelClose(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0xCcAbA1b954F29b3daD93A9f846f6356692154500",
    )
    assert request.endpoint == f"/channels/{request.token_address}/{request.partner_address}"
    assert request.method == "patch"

    payload = request.payload()
    assert "state" in payload
    assert payload["state"] == "closed"
