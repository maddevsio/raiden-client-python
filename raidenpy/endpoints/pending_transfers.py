from typing import Any, Dict, List

from raidenpy.endpoints import BaseRequest, BaseResponse
from raidenpy.types import Address, ChannelType


class PendingTransfersRequest(BaseRequest):
    """Returns a list of all transfers that have not been completed yet.

    GET /api/(version)/pending_transfers
    GET /api/(version)/pending_transfers/(token_address)
    GET /api/(version)/pending_transfers/(token_address)/(partner_address)
    """

    def __init__(self, token_address: Address = None, partner_address: Address = None):
        self.token_address = token_address
        self.partner_address = partner_address

    @property
    def endpoint(self) -> str:
        base = "/address"
        if self.token_address:
            base += f"/{self.token_address}"
            if self.partner_address:
                base += f"/{self.partner_address}"
        return base

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}


class PendingTransfersResponse(BaseResponse):
    """
    Response:
    [
        {
            "channel_identifier": "255",
            "initiator": "0x5E1a3601538f94c9e6D2B40F7589030ac5885FE7",
            "locked_amount": "119",
            "payment_identifier": "1",
            "role": "initiator",
            "target": "0x00AF5cBfc8dC76cd599aF623E60F763228906F3E",
            "token_address": "0xd0A1E359811322d97991E03f863a0C30C2cF029C",
            "token_network_address": "0x111157460c0F41EfD9107239B7864c062aA8B978",
            "transferred_amount": "331"
        }
    ]
    """

    def __init__(self, channels: List[ChannelType]):
        self.channels = channels

    def shema_validation(self) -> bool:
        return True

    def to_dict(self) -> List[Address]:
        return [ChannelType(channel) for channel in self.channels]

    @classmethod
    def from_dict(cls, d):
        cls.shema_validation(d)
        return cls(**d)
