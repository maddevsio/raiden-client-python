from requests import Request
from typing import Dict, Any
from raidenpy.api.request import BaseRequest, BaseResponse


class DeployTokenRequst(BaseRequest):
    """Registers a token.
    If a token is not registered yet (i.e.: A token network for that token does not exist in the registry),
    we need to register it by deploying a token network contract for that token.

    Doc: https://raiden-network.readthedocs.io/en/latest/rest_api.html#deploying
    """

    @property
    def endpoint(self) -> str:
        return "/tokens"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}


class PaymentRequiredException(Exception):
    pass


class NotFoundException(Exception):
    pass


class ConflictException(Exception):
    pass


class NotImplementedException(Exception):
    pass


class DeployTokenResponse(BaseResponse):

    def __init__(self, response: Request):
        self.response = response

    def validate_status_code(self, status_code: int) -> bool:
        if status_code == 201:
            return True

        if status_code == 402:
            raise PaymentRequiredException(
                "Insufficient ETH to pay for the gas of the register on-chain transaction"
            )

        if status_code == 404:
            raise NotFoundException(
                "he given token address is invalid."
            )

        if status_code == 409:
            raise ConflictException(
                "The token was already registered before, or the registering transaction failed."
            )

        if status_code == 501:
            raise NotImplementedException(
                "Registering a token only works on testnet temporarily. On mainnet this error is returned."
            )
        return False

    def to_dict(self) -> Dict[str, str]:
        self.validate_status_code(self.response.status_code)
        data = self.response.json()
        return {
            "token_network_address": data["token_network_address"]
        }
