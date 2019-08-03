from raiden_client.endpoints.mint_tokens import MintTokens


def test_mint_tokens_request() -> None:
    request = MintTokens(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        to="0xCcAbA1b954F29b3daD93A9f846f6356692154500",
        value=10,
    )
    assert request.endpoint == f"/_testing/tokens/{request.token_address}/mint"
    assert request.method == "post"
    payload = request.payload()
    assert "to" in payload
    assert "value" in payload
    assert "contract_method" in payload
    assert payload["contract_method"] == "mintFor"


def test_mint_tokens_method_request() -> None:
    request = MintTokens(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        to="0xCcAbA1b954F29b3daD93A9f846f6356692154500",
        value=10,
        contract_method="mint",
    )
    assert request.endpoint == f"/_testing/tokens/{request.token_address}/mint"
    assert request.method == "post"
    payload = request.payload()
    assert "to" in payload
    assert "value" in payload
    assert "contract_method" in payload
    assert payload["contract_method"] == "mint"
