from raiden_client.endpoints.channel_open import ChannelOpen


def test_channel_open_request() -> None:
    request = ChannelOpen(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0xCcAbA1b954F29b3daD93A9f846f6356692154500",
        total_deposit=35000000,
        settle_timeout=500,
    )
    assert request.endpoint == "/channels"
    assert request.method == "put"
    assert request.name == "channel-open"
    assert "token_address" in request.payload()
    assert "partner_address" in request.payload()
    assert "total_deposit" in request.payload()
    assert "settle_timeout" in request.payload()
