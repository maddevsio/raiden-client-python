from raiden_client.endpoints.mint_tokens import MintTokensRequest, MintTokensResponse


def test_mint_tokens_request():
    request = MintTokensRequest(token_address="0x123", to="0x321", value=10)
    assert request.endpoint == f"/_testing/tokens/{request.token_address}/mint"
    assert request.method == "post"
    payload = request.payload()
    assert "to" in payload
    assert "value" in payload
    assert "contract_method" in payload
    assert payload["contract_method"] == "mintFor"


def test_mint_tokens_method_request():
    request = MintTokensRequest(token_address="0x123", to="0x321", value=10, contract_method="mint")
    assert request.endpoint == f"/_testing/tokens/{request.token_address}/mint"
    assert request.method == "post"
    payload = request.payload()
    assert "to" in payload
    assert "value" in payload
    assert "contract_method" in payload
    assert payload["contract_method"] == "mint"


def test_mint_token_Response():
    response = MintTokensResponse.from_dict({
        "transaction_hash": "0x123123"
    })
    assert "transaction_hash" in response.to_dict()
