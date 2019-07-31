from typing import Any, Dict

from raiden_client.endpoints import BaseRequest, BaseResponse
from raiden_client.types import Address, ChannelType


class ChannelOpenRequest(BaseRequest):
    """Opens / creates a channel
    Args:
        - token_address (address)   – The token we want to be used in the channel.
        - partner_address (address) – The partner we want to open a channel with.
        - total_deposit (int)       – Total amount of tokens to be deposited to the channel
        - settle_timeout (int)      – The amount of blocks that the settle timeout should have.

    PUT /api/(version)/channels
    """

    def __init__(
        self, token_address: Address, partner_address: Address, total_deposit: int, settle_timeout: int
    ) -> None:
        # TODO: EIP-55 token encode
        self.token_address = token_address
        self.partner_address = partner_address
        self.total_deposit = total_deposit
        self.settle_timeout = settle_timeout

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


class ChannelOpenResponse(BaseResponse):
    """Return Channel object."""

    def __init__(self, channel: ChannelType):
        self.channel = channel

    def to_dict(self) -> Dict[str, ChannelType]:
        return {"channel": self.channel}

    @classmethod
    def from_dict(cls, d: Dict[str, ChannelType]) -> BaseResponse:
        return cls(channel=d["channel"])
