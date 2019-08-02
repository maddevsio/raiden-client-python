from raiden_client.plugins.v1.non_settled_partners import NonSettledPartnersPlugin


def test_non_settled_partners_request() -> None:
    request = NonSettledPartnersPlugin(token_address="0x145737846791E749f96344135Ce211BE8C510a17")
    assert request.endpoint == f"/tokens/{request.token_address}/partners"
    assert request.method == "get"
    assert not request.payload()
