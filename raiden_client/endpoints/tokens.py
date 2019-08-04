from typing import Any, Dict, List

from raiden_client import utils
from raiden_client.endpoints import BaseEndpoint


class Tokens(BaseEndpoint):
    """Returns a list of addresses of all registered tokens.

    GET /api/(version)/tokens
    https://raiden-network.readthedocs.io/en/latest/rest_api.html#get--api-(version)-tokens

    GET /api/(version)/tokens/(token_address)
    https://raiden-network.readthedocs.io/en/latest/rest_api.html#get--api-(version)-tokens-(token_address)
    """
    tokens = None

    def __init__(self, token_address: str = None) -> None:
        self.token_address = utils.normalize_address_eip55(token_address)

    @property
    def name(self) -> str:
        return "tokens"

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

    # have to ignore type, some API endpoints returs list not dict
    def from_dict(self, response: List[str]) -> None:   # type: ignore
        self.tokens = response

    def to_dict(self) -> Dict[str, List[str]]:
        return {"tokens": self.tokens}
