from typing import Any, Dict

from raidenpy.types import Address
from raidenpy.endpoints import BaseRequest, BaseResponse


class AddressRequest(BaseRequest):
    """Querying Information About Your Raiden Node

    Raiden address is the same address as the Ethereum
    address chosen, when starting the Raiden node

    GET /api/(version)/address
    https://raiden-network.readthedocs.io/en/latest/rest_api.html#querying-information-about-your-raiden-node
    """

    @property
    def endpoint(self) -> str:
        return "/address"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}


class AddressResponse(BaseResponse):
    """Address Response.
    {
        "our_address": "0x2a65Aca4D5fC5B5C859090a6c34d164135398226"
    }
    """
    def __init__(self, our_address: Address):
        self.our_address = our_address

    def shema_validation(self):
        # Validate input json schema
        return True

    @classmethod
    def from_dict(cls, d):
        cls.shema_validation(d)
        return cls(**d)

    def to_dict(self) -> Dict[str, str]:
        return {
            "our_address": self.our_address
        }
