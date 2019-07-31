from typing import Any, Dict

from raiden_client.endpoints import BaseRequest, BaseResponse
from raiden_client.types import Address, ChannelType


class ChannelCloseRequest(BaseRequest):
    """Close a channel.

    PATCH /api/(version)/channels/(token_address)/(partner_address)
    """

    def __init__(self, token_address: Address, partner_address: Address) -> None:
        # TODO: EIP-55 token encode
        self.token_address = token_address
        self.partner_address = partner_address

    @property
    def endpoint(self) -> str:
        return f"/channels/{self.token_address}/{self.partner_address}"

    @property
    def method(self) -> str:
        return "patch"

    def payload(self) -> Dict[str, Any]:
        """The only valid choice is "closed."""
        return {"state": "closed"}


class ChannelCloseResponse(BaseResponse):
    """Return Channel object."""

    def __init__(self, channel: ChannelType):
        self.channel = channel

    def to_dict(self) -> Dict[str, ChannelType]:
        return {"channel": self.channel}

    @classmethod
    def from_dict(cls, d: Dict[str, ChannelType]) -> BaseResponse:
        return cls(channel=d["channel"])
