from typing import Any, Dict

from raidenpy.endpoints import BaseRequest, BaseResponse
from raidenpy.types import Address


class TokenNetworkRequest(BaseRequest):
    """Returns the address of the corresponding token network for the given token

    If the token is registered.
    GET /api/(version)/tokens/(token_address)
    """

    def __init__(self, token_address: Address):
        # TODO: EIP-55 token encode
        self.token_address = token_address

    @property
    def endpoint(self) -> str:
        return f"/tokens/{self.token_address}"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}


class TokenNetworkResponse(BaseResponse):
    """
    Response:
    "0x61bB630D3B2e8eda0FC1d50F9f958eC02e3969F6"
    """

    def __init__(self, token_network_address: Address):
        self.token_network_address = token_network_address

    def to_dict(self) -> Dict[str, Address]:
        return {"token_network_address": Address(self.token_network_address)}

    def shema_validation(self) -> bool:
        return True

    @classmethod
    def from_dict(cls, d):
        cls.shema_validation(d)
        return cls(**d)
