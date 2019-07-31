from raidenpy.endpoints.address import AddressRequest
from raidenpy.endpoints.address import AddressResponse
from raidenpy.types import Address


def test_address():
    address = AddressRequest()
    assert address.endpoint == "/address"
    assert address.method == "get"
    assert not address.payload()


def test_address_response_status_code():
    resp = AddressResponse(our_address=Address("0x123"))
    assert resp.to_dict() == {"our_address": "0x123"}
