from raidenpy.endpoints.token_register import TokenRegistryRequest


def test_deploy_tokens():
    token_address = "0x123"
    request = TokenRegistryRequest(token_address=token_address)
    assert request.endpoint == f"/tokens/{token_address}"
    assert request.method == "put"
    assert not request.payload()
