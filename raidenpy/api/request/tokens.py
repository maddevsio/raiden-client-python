from typing import Dict, List, Any

from requests import Response
from raidenpy.types import Address

from raidenpy.api.request import BaseRequest, BaseResponse


class TokensRequest(BaseRequest):
    """Query a list of addresses of all registered tokens"""

    @property
    def endpoint(self) -> str:
        return "/tokens"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}


class TokensResponse(BaseResponse):
    """Returns a list of addresses of all registered tokens."""

    def __init__(self, response: Response):
        self.response = response

    def validate_status_code(self, status_code: int) -> bool:
        if status_code != 200:
            raise Exception()
        return True

    def to_dict(self) -> List[Address]:
        self.validate_status_code(self.response.status_code)
        data = self.response.json()
        return [Address(item) for item in data]
