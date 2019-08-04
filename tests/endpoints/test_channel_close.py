from raiden_client.endpoints.channel_close import ChannelClose


def test_channel_close_request() -> None:
    endpoint = ChannelClose(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0xCcAbA1b954F29b3daD93A9f846f6356692154500",
    )
    assert endpoint.endpoint == f"/channels/{endpoint.token_address}/{endpoint.partner_address}"
    assert endpoint.method == "patch"
    assert endpoint.name == "channel-close"

    payload = endpoint.payload()
    assert "state" in payload
    assert payload["state"] == "closed"
