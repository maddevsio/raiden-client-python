from typing import Any, Dict

from raiden_client.endpoints import BaseRequest, BaseResponse
from raiden_client.types import Address, ChannelType


class ChannelRequest(BaseRequest):
    """Query information about one of your channels.

    The channel is specified by the address of the token and the partner’s address.

    GET /api/(version)/channels/(token_address)/(partner_address)
    """

    def __init__(self, token_address: Address, partner_address: Address):
        # TODO: EIP-55 token encode
        self.token_address = token_address
        self.partner_address = partner_address

    @property
    def endpoint(self) -> str:
        return f"/channels/{self.token_address}/{self.partner_address}"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}


class ChannelResponse(BaseResponse):
    """Returns a list of all unsettled channels."""

    def __init__(self, channel: ChannelType):
        self.channel = channel

    def to_dict(self) -> Dict[str, ChannelType]:
        return {"channel": self.channel}

    @classmethod
    def from_dict(cls, d: Dict[str, ChannelType]) -> "ChannelResponse":
        return cls(channel=d["channel"])
