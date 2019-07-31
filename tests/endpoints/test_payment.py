from raiden_client.endpoints.payment import PaymentRequest

# TODO: review PaymentResponse object and write tests


def test_payment_request():
    request = PaymentRequest(token_address="0x123", target_address="0x321", amount=10)
    assert request.endpoint == f"/payments/{request.token_address}/{request.target_address}"
    assert request.method == "post"
    payload = request.payload()
    assert "amount" in payload
    assert "identifier" not in payload


def test_payment_request_identifier():
    req = PaymentRequest(token_address="0x123", target_address="0x321", amount=10, identifier=1)
    assert req.endpoint == f"/payments/{req.token_address}/{req.target_address}"
    assert req.method == "post"
    payload = req.payload()
    assert "amount" in payload
    assert "identifier" in payload
