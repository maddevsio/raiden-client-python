from raiden_client.endpoints.channel_withdraw import ChannelWithdraw


def test_channel_withdraw_request() -> None:
    request = ChannelWithdraw(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0xCcAbA1b954F29b3daD93A9f846f6356692154500",
        total_withdraw=200,
    )
    assert request.endpoint == f"/channels/{request.token_address}/{request.partner_address}"
    assert request.method == "patch"

    payload = request.payload()
    assert "total_withdraw" in payload
    assert payload["total_withdraw"] == 200
