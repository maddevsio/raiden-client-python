from raiden_client.endpoints.payment_events import PaymentEventsRequest, PaymentEventsResponse


def test_payment_events_request():
    request = PaymentEventsRequest(token_address="0x123", target_address="0x321")
    assert request.endpoint == f"/payments/{request.token_address}/{request.target_address}"
    assert request.method == "get"
    assert not request.payload()


def test_payment_events_response():
    response = PaymentEventsResponse.from_dict({
        "payment_events": []
    })
    assert "payment_events" in response.to_dict()
