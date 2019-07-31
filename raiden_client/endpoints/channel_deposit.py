from typing import Any, Dict

from raiden_client.endpoints import BaseRequest, BaseResponse
from raiden_client.types import Address, ChannelType


class ChannelDepositRequest(BaseRequest):
    """Increase the deposit in channel.

    PATCH /api/(version)/channels/(token_address)/(partner_address)
    """

    def __init__(self, token_address: Address, partner_address: Address, total_deposit: int) -> None:
        # TODO: EIP-55 token encode
        self.token_address = token_address
        self.partner_address = partner_address
        self.total_deposit = total_deposit

    @property
    def endpoint(self) -> str:
        return f"/channels/{self.token_address}/{self.partner_address}"

    @property
    def method(self) -> str:
        return "patch"

    def payload(self) -> Dict[str, Any]:
        return {"total_deposit": self.total_deposit}


class ChannelDepositResponse(BaseResponse):
    """Return Channel object."""

    def __init__(self, channel: ChannelType):
        self.channel = channel

    def to_dict(self) -> Dict[str, ChannelType]:
        return {"channel": self.channel}

    @classmethod
    def from_dict(cls, d: Dict[str, ChannelType]) -> BaseResponse:
        return cls(channel=d["channel"])
