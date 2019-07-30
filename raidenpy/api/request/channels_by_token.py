from typing import Dict, List, Any

from requests import Response
from raidenpy.types import ChannelType, Address

from raidenpy.exceptions import (
    InternalServerException,
    ResponseStatusCodeException,
    NotFoundException,
)
from raidenpy.api.request import BaseRequest, BaseResponse


class ChannelByTokenRequest(BaseRequest):
    """Request a list of all unsettled channels for the given token address.

    GET /api/(version)/channels/(token_address)
    """

    def __init__(self, token_address: Address):
        # TODO: EIP-55 token encode
        self.token_address = token_address

    @property
    def endpoint(self) -> str:
        return f"/channels/{self.token_address}"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}


class ChannelByTokenResponse(BaseResponse):
    """Returns a list of all unsettled channels."""

    def __init__(self, response: Response):
        self.response = response

    def validate_status_code(self, status_code: int) -> bool:
        if status_code == 200:
            return True
        elif status_code == 404:
            raise NotFoundException(
                "HTTP 404: The given token address is not a valid eip55-encoded Ethereum address"
            )
        elif status_code == 500:
            raise InternalServerException("HTTP 500: Internal Raiden node error")
        raise ResponseStatusCodeException(f"HTTP {status_code}: Unhandled status code")

    def to_dict(self) -> List[ChannelType]:
        self.validate_status_code(self.response.status_code)
        data = self.response.json()
        return [ChannelType(item) for item in data]
