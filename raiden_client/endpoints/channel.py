from typing import Any, Dict

from raiden_client import utils
from raiden_client.endpoints import BaseEndpoint


class Channel(BaseEndpoint):
    """Query information about one of your channels.

    The channel is specified by the address of the token and the partner’s address.

    GET /api/(version)/channels/(token_address)/(partner_address)
    """

    channel = None

    def __init__(self, token_address: str, partner_address: str) -> None:
        self.token_address = utils.normalize_address_eip55(token_address)
        self.partner_address = utils.normalize_address_eip55(partner_address)

    @property
    def name(self) -> str:
        return "channel"

    @property
    def endpoint(self) -> str:
        return f"/channels/{self.token_address}/{self.partner_address}"

    @property
    def method(self) -> str:
        return "get"

    @classmethod
    def payload(cls) -> Dict[str, Any]:
        return {}

    def from_dict(self, response: Dict[str, Any]) -> None:
        self.channel = response

    def to_dict(self) -> Dict[str, Any]:
        return {"channel": self.channel}
