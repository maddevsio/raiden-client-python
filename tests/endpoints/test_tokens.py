from raiden_client.endpoints.tokens import TokensRequest, TokensResponse
from raiden_client.types import Address


def test_tokens():
    request = TokensRequest()
    assert request.endpoint == "/tokens"
    assert request.method == "get"
    assert not request.payload()


def test_tokens_in_tokens_network():
    request = TokensRequest(token_address=Address("0x123"))
    assert request.endpoint == "/tokens/0x123"
    assert request.method == "get"
    assert not request.payload()


def test_token_response():
    response = TokensResponse.from_dict({"tokens": []})
    assert "tokens" in response.to_dict()
