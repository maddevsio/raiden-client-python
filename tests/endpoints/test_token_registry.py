from raidenpy.endpoints.token_register import (
    TokenRegistryRequest,
    TokenRegistryResponse,
)


def test_registry_token_request():
    token_address = "0x123"
    request = TokenRegistryRequest(token_address=token_address)
    assert request.endpoint == f"/tokens/{token_address}"
    assert request.method == "put"
    assert not request.payload()


def test_registry_token_response():
    response = TokenRegistryResponse.from_dict({"token_network_address": "0x123"})
    assert "token_network_address" in response.to_dict()
