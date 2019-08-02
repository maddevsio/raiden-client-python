from raiden_client.plugins.v1.payment_events import PaymentEventsPlugin


def test_payment_events_request():
    request = PaymentEventsPlugin(token_address="0x145737846791E749f96344135Ce211BE8C510a17", target_address="0xCcAbA1b954F29b3daD93A9f846f6356692154500")
    assert request.endpoint == f"/payments/{request.token_address}/{request.target_address}"
    assert request.method == "get"
    assert not request.payload()
