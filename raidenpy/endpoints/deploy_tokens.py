from typing import Any, Dict

from requests import Response

from raidenpy.endpoints import BaseRequest, BaseResponse
from raidenpy.exceptions import (
    ConflictException,
    NotFoundException,
    NotImplementedException,
    PaymentRequiredException,
    ResponseStatusCodeException,
)
from raidenpy.types import Address


class DeployTokenRequst(BaseRequest):
    """Registers a token.
    If a token is not registered yet (i.e.: A token network for that token does not exist in the registry),
    we need to register it by deploying a token network contract for that token.

    PUT /api/(version)/tokens/(token_address)
    Doc: https://raiden-network.readthedocs.io/en/latest/rest_api.html#deploying
    """

    def __init__(self, token_address: str) -> None:
        self.token_address = token_address

    @property
    def endpoint(self) -> str:
        return f"/tokens/{self.token_address}"

    @property
    def method(self) -> str:
        return "put"

    def payload(self) -> Dict[str, Any]:
        return {}


class DeployTokenResponse(BaseResponse):
    def __init__(self, response: Response):
        self.response = response

    def validate_status_code(self, status_code: int) -> bool:
        if status_code == 201:
            return True

        if status_code == 402:
            raise PaymentRequiredException(
                "HTTP 402: Insufficient ETH to pay for the gas of the register on-chain transaction"
            )

        if status_code == 404:
            raise NotFoundException("HTTP 404: The given token address is invalid.")

        if status_code == 409:
            raise ConflictException(
                "HTTP 409: The token was already registered before, or the registering transaction failed."
            )

        if status_code == 501:
            raise NotImplementedException(
                "HTTP 501: Registering a token only works on testnet temporarily. " "On mainnet this error is returned."
            )
        raise ResponseStatusCodeException(f"{status_code}: Unhandled status code")

    def to_dict(self) -> Dict[str, Address]:
        self.validate_status_code(self.response.status_code)
        return self.response.json()
