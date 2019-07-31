from typing import Any, Dict, List

from raiden_client.endpoints import BaseRequest, BaseResponse
from raiden_client.types import Address, ChannelType


class ChannelsRequest(BaseRequest):
    """Request a list of all unsettled channels.
    GET /api/(version)/channels

    All channels for the given token address
    GET /api/(version)/channels/(token_address)
    """

    def __init__(self, token_address: Address = None):
        self.token_address = token_address

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


class ChannelsResponse(BaseResponse):
    """Returns a list of all unsettled channels."""

    def __init__(self, channels: List[ChannelType]):
        self.channels = channels

    def to_dict(self) -> Dict[str, List[ChannelType]]:
        return {"channels": self.channels}

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "ChannelsResponse":
        return cls(channels=d["channels"])
