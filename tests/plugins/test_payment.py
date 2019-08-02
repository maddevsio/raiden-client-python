from raiden_client.plugins.v1.payment import PaymentPlugin


def test_payment_request():
    request = PaymentPlugin(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        target_address="0xCcAbA1b954F29b3daD93A9f846f6356692154500",
        amount=10,
    )
    assert request.endpoint == f"/payments/{request.token_address}/{request.target_address}"
    assert request.method == "post"
    payload = request.payload()
    assert "amount" in payload
    assert "identifier" not in payload


def test_payment_request_identifier():
    req = PaymentPlugin(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        target_address="0xCcAbA1b954F29b3daD93A9f846f6356692154500",
        amount=10,
        identifier=1,
    )
    assert req.endpoint == f"/payments/{req.token_address}/{req.target_address}"
    assert req.method == "post"
    payload = req.payload()
    assert "amount" in payload
    assert "identifier" in payload
