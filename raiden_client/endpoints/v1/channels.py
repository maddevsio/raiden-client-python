from typing import Any, Dict

from raiden_client import utils
from raiden_client.endpoints.v1 import BaseV1Endpoint


class Channels(BaseV1Endpoint):
    """Request a list of all unsettled channels.

    GET /api/(version)/channels

    All channels for the given token address
    GET /api/(version)/channels/(token_address)
    """

    channels = None

    def __init__(self, token_address: str = None) -> None:
        self.token_address = utils.normalize_address_eip55(token_address)

    @property
    def name(self) -> str:
        return "channels"

    @property
    def endpoint(self) -> str:
        if self.token_address:
            return f"/channels/{self.token_address}"
        return "/channels"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}

    def from_dict(self, response: Dict[str, Any]) -> None:
        self.channels = response

    def to_dict(self) -> Dict[str, Any]:
        return {"channels": self.channels}
