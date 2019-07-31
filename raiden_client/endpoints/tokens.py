from typing import Any, Dict, List

from raiden_client.endpoints import BaseRequest, BaseResponse
from raiden_client.types import Address


class TokensRequest(BaseRequest):
    """Query a list of addresses of all registered tokens

    - Query list all tokens addresses
    GET /api/(version)/tokens

    - Query address of the token network for the given token
    GET /api/(version)/tokens/(token_address)
    """

    def __init__(self, token_address: Address = None):
        self.token_address = token_address

    @property
    def endpoint(self) -> str:
        if self.token_address:
            return f"/tokens/{self.token_address}"
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

    def to_dict(self) -> List[Address]:
        return {"tokens": self.tokens}

    @classmethod
    def from_dict(cls, d):
        return cls(tokens=d["tokens"])
