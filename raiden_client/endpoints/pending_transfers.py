from typing import Any, Dict, List

from raiden_client.endpoints import BaseRequest, BaseResponse
from raiden_client.types import Address, PendingTransfer


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
        if self.token_address and self.partner_address:
            return f"/pending_transfers/{self.token_address}/{self.partner_address}"

        if self.token_address:
            return f"/pending_transfers/{self.token_address}"

        return "/pending_transfers"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}


class PendingTransfersResponse(BaseResponse):
    def __init__(self, pending_transfers: List[PendingTransfer]):
        self.pending_transfers = pending_transfers

    def to_dict(self) -> Dict[str, List[PendingTransfer]]:
        return {"pending_transfers": self.pending_transfers}

    @classmethod
    def from_dict(cls, d: Dict[str, List[PendingTransfer]]) -> BaseResponse:
        return cls(pending_transfers=d["pending_transfers"])
