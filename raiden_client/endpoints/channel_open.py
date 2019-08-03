from typing import Any, Dict

from raiden_client import utils
from raiden_client.endpoints import BaseEndpoint


class ChannelOpen(BaseEndpoint):
    """Opens / creates a channel

    PUT /api/(version)/channels
    """
    channel = None

    def __init__(self, token_address: str, partner_address: str, total_deposit: int, settle_timeout: int) -> None:
        """
        :params: token_address (address)   – The token we want to be used in the channel.
        :params: partner_address (address) – The partner we want to open a channel with.
        :params: total_deposit (int)       – Total amount of tokens to be deposited to the channel
        :params: settle_timeout (int)      – The amount of blocks that the settle timeout should have.
        """
        self.token_address = utils.normalize_address_eip55(token_address)
        self.partner_address = utils.normalize_address_eip55(partner_address)
        self.total_deposit = total_deposit
        self.settle_timeout = settle_timeout

    @property
    def name(self) -> str:
        return "channel-open"

    @property
    def endpoint(self) -> str:
        return f"/channels"

    @property
    def method(self) -> str:
        return "put"

    def payload(self) -> Dict[str, Any]:
        return {
            "token_address": self.token_address,
            "partner_address": self.partner_address,
            "total_deposit": self.total_deposit,
            "settle_timeout": self.settle_timeout,
        }

    def from_dict(self, response: Dict[str, Any]) -> None:
        self.channel = response

    def to_dict(self) -> Dict[str, Any]:
        return {"channel": self.channel}
