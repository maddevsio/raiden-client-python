from typing import Any, Dict

from requests import Response

from raidenpy.endpoints import BaseRequest, BaseResponse
from raidenpy.exceptions import InternalServerException, NotFoundException, ResponseStatusCodeException
from raidenpy.types import Address, ChannelType


class ChannelRequest(BaseRequest):
    """Query information about one of your channels.

    The channel is specified by the address of the token and the partner’s address.

    GET /api/(version)/channels/(token_address)/(partner_address)
    """

    def __init__(self, token_address: Address, partner_address: Address):
        # TODO: EIP-55 token encode
        self.token_address = token_address
        self.partner_address = partner_address

    @property
    def endpoint(self) -> str:
        return f"/channels/{self.token_address}/{self.partner_address}"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}


class ChannelResponse(BaseResponse):
    """Returns a list of all unsettled channels."""

    def __init__(self, response: Response):
        self.response = response

    def validate_status_code(self, status_code: int) -> bool:
        if status_code == 200:
            return True
        elif status_code == 404:
            raise NotFoundException(
                "HTTP 404: The given token address is not a valid eip55-encoded Ethereum address, "
                "or The channel does not exist"
            )
        elif status_code == 500:
            raise InternalServerException("HTTP 500: Internal Raiden node error")
        raise ResponseStatusCodeException(f"HTTP {status_code}: Unhandled status code")

    def to_dict(self) -> ChannelType:
        self.validate_status_code(self.response.status_code)
        data = self.response.json()
        return ChannelType(data)
