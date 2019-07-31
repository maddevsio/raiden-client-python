from raidenpy.endpoints.deploy_tokens import DeployTokenRequst


def test_deploy_tokens():
    token_address = "0x123"
    request = DeployTokenRequst(token_address=token_address)
    assert request.endpoint == f"/tokens/{token_address}"
    assert request.method == "put"
    assert not request.payload()