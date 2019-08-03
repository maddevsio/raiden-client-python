from typing import Any, Dict

from raiden_client import utils
from raiden_client.endpoints.v1 import BaseV1Endpoint


class TokenRegister(BaseV1Endpoint):
    """Registers a token.
    If a token is not registered yet (i.e.: A token network for that token does not exist in the registry),
    we need to register it by deploying a token network contract for that token.

    PUT /api/(version)/tokens/(token_address)
    Doc: https://raiden-network.readthedocs.io/en/latest/rest_api.html#deploying
    """
    token_network_address = None

    def __init__(self, token_address: str = None) -> None:
        self.token_address = utils.normalize_address_eip55(token_address)

    @property
    def name(self) -> str:
        return "token-register"

    @property
    def endpoint(self) -> str:
        return f"/tokens/{self.token_address}"

    @property
    def method(self) -> str:
        return "put"

    def payload(self) -> Dict[str, Any]:
        return {}

    def from_dict(self, response: Dict[str, Any]) -> None:
        self.token_network_address = response

    def to_dict(self) -> Dict[str, Any]:
        return {"token_network_address": self.token_network_address}
