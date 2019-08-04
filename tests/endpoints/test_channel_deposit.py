from raiden_client.endpoints.channel_deposit import ChannelDeposit


def test_channel_deposit_endpoint() -> None:
    endpoint = ChannelDeposit(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0xCcAbA1b954F29b3daD93A9f846f6356692154500",
        total_deposit=2000,
    )
    assert endpoint.endpoint == f"/channels/{endpoint.token_address}/{endpoint.partner_address}"
    assert endpoint.method == "patch"
    assert endpoint.name == "deposit-increase"

    payload = endpoint.payload()
    assert "total_deposit" in payload
    assert payload["total_deposit"] == 2000
