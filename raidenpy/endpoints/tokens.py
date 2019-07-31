from typing import Any, Dict, List

from requests import Response

from raidenpy.endpoints import BaseRequest, BaseResponse
from raidenpy.types import Address


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

    def __init__(self, tokens: List[Address]):
        self.tokens = tokens

    def shema_validation(self) -> bool:
        return True

    def to_dict(self) -> List[Address]:
        return [Address(token) for token in self.tokens]

    @classmethod
    def from_dict(cls, d):
        cls.shema_validation(d)
        return cls(**d)
