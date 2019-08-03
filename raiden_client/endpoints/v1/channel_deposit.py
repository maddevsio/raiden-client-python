from typing import Any, Dict

from raiden_client import utils
from raiden_client.endpoints.v1 import BaseV1Endpoint


class ChannelDeposit(BaseV1Endpoint):
    """Increase the deposit in channel.

    PATCH /api/(version)/channels/(token_address)/(partner_address)
    """
    channel = None

    def __init__(self, token_address: str, partner_address: str, total_deposit: int) -> None:
        self.token_address = utils.normalize_address_eip55(token_address)
        self.partner_address = utils.normalize_address_eip55(partner_address)
        self.total_deposit = total_deposit

    @property
    def name(self) -> str:
        return "channel"

    @property
    def endpoint(self) -> str:
        return f"/channels/{self.token_address}/{self.partner_address}"

    @property
    def method(self) -> str:
        return "patch"

    def payload(self) -> Dict[str, Any]:
        return {"total_deposit": self.total_deposit}

    def from_dict(self, response: Dict[str, Any]) -> None:
        self.channel = response

    def to_dict(self) -> Dict[str, Any]:
        return {"channel": self.channel}
