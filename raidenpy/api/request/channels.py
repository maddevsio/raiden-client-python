from typing import Any, Dict, List

from requests import Response

from raidenpy.api.request import BaseRequest, BaseResponse
from raidenpy.exceptions import InternalServerException, ResponseStatusCodeException
from raidenpy.types import ChannelType


class ChannelsRequest(BaseRequest):
    """Request a list of all unsettled channels.
    GET /api/(version)/channels
    """

    @property
    def endpoint(self) -> str:
        return "/channels"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}


class ChannelsResponse(BaseResponse):
    """Returns a list of all unsettled channels."""

    def __init__(self, response: Response):
        self.response = response

    def validate_status_code(self, status_code: int) -> bool:
        if status_code == 200:
            return True
        elif status_code == 500:
            raise InternalServerException("Internal Raiden node error")
        raise ResponseStatusCodeException(f"{status_code}: Unhandled status code")

    def to_dict(self) -> List[ChannelType]:
        self.validate_status_code(self.response.status_code)
        data = self.response.json()
        return [ChannelType(item) for item in data]
