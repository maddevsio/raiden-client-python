from typing import Any, Dict

from requests import Response

from raidenpy.api.request import BaseRequest, BaseResponse
from raidenpy.exceptions import NotFoundException, ResponseStatusCodeException
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
    def __init__(self, response: Response):
        self.response = response

    def validate_status_code(self, status_code: int) -> bool:
        if status_code == 200:
            return True
        elif status_code == 404:
            raise NotFoundException("HTTP 404: No token network found for the provided token address")
        raise ResponseStatusCodeException(f"HTTP {status_code}: Unhandled status code")

    def to_dict(self) -> Address:
        self.validate_status_code(self.response.status_code)
        data = self.response.json()
        return Address(data)
