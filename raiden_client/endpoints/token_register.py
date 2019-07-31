from typing import Any, Dict

from raiden_client.endpoints import BaseRequest, BaseResponse
from raiden_client.types import Address


class TokenRegistryRequest(BaseRequest):
    """Registers a token.
    If a token is not registered yet (i.e.: A token network for that token does not exist in the registry),
    we need to register it by deploying a token network contract for that token.

    PUT /api/(version)/tokens/(token_address)
    Doc: https://raiden-network.readthedocs.io/en/latest/rest_api.html#deploying
    """

    def __init__(self, token_address: Address):
        # TODO: EIP-55 token encode
        self.token_address = token_address

    @property
    def endpoint(self) -> str:
        return f"/tokens/{self.token_address}"

    @property
    def method(self) -> str:
        return "put"

    def payload(self) -> Dict[str, Any]:
        return {}


class TokenRegistryResponse(BaseResponse):
    """
    Response:
    "0x61bB630D3B2e8eda0FC1d50F9f958eC02e3969F6"
    """

    def __init__(self, token_network_address: Address):
        self.token_network_address = token_network_address

    def to_dict(self) -> Dict[str, Address]:
        return {"token_network_address": Address(self.token_network_address)}

    @classmethod
    def from_dict(cls, d: Dict[str, Address]) -> BaseResponse:
        return cls(token_network_address=d["token_network_address"])
