from raiden_client.plugins.v1.pending_transfers import PendingTransfersPlugin


def test_pending_transfers() -> None:
    request = PendingTransfersPlugin()
    assert request.endpoint == "/pending_transfers"
    assert request.method == "get"
    assert not request.payload()


def test_pending_transfers_specified_token() -> None:
    token_address = "0x145737846791E749f96344135Ce211BE8C510a17"
    request = PendingTransfersPlugin(token_address=token_address)
    assert request.endpoint == f"/pending_transfers/{token_address}"


def test_pending_transfers_specified_token_channel() -> None:
    token_address = "0x145737846791E749f96344135Ce211BE8C510a17"
    partner_address = "0xCcAbA1b954F29b3daD93A9f846f6356692154500"
    request = PendingTransfersPlugin(token_address=token_address, partner_address=partner_address)
    assert request.endpoint == f"/pending_transfers/{token_address}/{partner_address}"
