from raidenpy.types import Address
from raidenpy.endpoints.non_settled_partners import NonSettledPartnersRequest, NonSettledPartnersResponse


def test_non_settled_partners_request():
    request = NonSettledPartnersRequest(
        token_address=Address("0x123")
    )
    assert request.endpoint == "/tokens/0x123/partners"
    assert request.method == "get"
    assert not request.payload()


def test_non_settled_partners_response():
    response = NonSettledPartnersResponse.from_dict({
        "non_settled_partners": []
    })
    assert "non_settled_partners" in response.to_dict()
