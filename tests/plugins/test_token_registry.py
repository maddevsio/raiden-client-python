from raiden_client.endpoints.token_registry import TokenRegister


def test_registry_token_request() -> None:
    token_address = "0x145737846791E749f96344135Ce211BE8C510a17"
    request = TokenRegister(token_address=token_address)
    assert request.endpoint == f"/tokens/{token_address}"
    assert request.method == "put"
    assert not request.payload()
