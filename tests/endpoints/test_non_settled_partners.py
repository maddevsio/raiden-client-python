from raiden_client.endpoints.non_settled_partners import NonSettledPartners


def test_non_settled_partners_request() -> None:
    request = NonSettledPartners(token_address="0x145737846791E749f96344135Ce211BE8C510a17")
    assert request.endpoint == f"/tokens/{request.token_address}/partners"
    assert request.method == "get"
    assert request.name == "non-settled"
    assert not request.payload()
