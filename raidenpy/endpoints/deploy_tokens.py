from typing import Any, Dict

from raidenpy.endpoints import BaseRequest, BaseResponse
from raidenpy.exceptions import (
    ConflictException,
    NotFoundException,
    NotImplementedException,
    PaymentRequiredException,
)
from raidenpy.types import Address


class DeployTokenRequst(BaseRequest):
    """Registers a token.
    If a token is not registered yet (i.e.: A token network for that token does not exist in the registry),
    we need to register it by deploying a token network contract for that token.

    PUT /api/(version)/tokens/(token_address)
    Doc: https://raiden-network.readthedocs.io/en/latest/rest_api.html#deploying
    """

    def __init__(self, token_address: Address) -> None:
        self.token_address = token_address

    status_codes = {
        402: PaymentRequiredException("Insufficient ETH to pay for the gas of the register on-chain transaction"),
        404: NotFoundException("HTTP 404: The given token address is invalid."),
        409: ConflictException("HTTP 409: The token was already registered before or the registering "
                               "transaction failed"),
        501: NotImplementedException("HTTP 501: Registering a token only works on testnet temporarily. "
                                     "On mainnet this error is returned."),
    }

    @property
    def endpoint(self) -> str:
        return f"/tokens/{self.token_address}"

    @property
    def method(self) -> str:
        return "put"

    def payload(self) -> Dict[str, Any]:
        return {}


class DeployTokenResponse(BaseResponse):
    """
    Response:
    {
        "token_network_address": "0xC4F8393fb7971E8B299bC1b302F85BfFB3a1275a"
    }
    """
    def __init__(self, token_network_address: Address):
        self.token_network_address = token_network_address

    def to_dict(self) -> Dict[str, Address]:
        return {
            "token_network_address": self.token_network_address
        }

    def shema_validation(self) -> bool:
        return True

    @classmethod
    def from_dict(cls, d):
        cls.shema_validation(d)
        return cls(**d)
