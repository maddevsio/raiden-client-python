from typing import Any, Dict

from raiden_client import utils
from raiden_client.endpoints import BaseEndpoint


class PendingTransfers(BaseEndpoint):
    """Returns a list of all transfers that have not been completed yet.

    GET /api/(version)/pending_transfers
    GET /api/(version)/pending_transfers/(token_address)
    GET /api/(version)/pending_transfers/(token_address)/(partner_address)
    """
    pending_transfers = None

    def __init__(self, token_address: str = None, partner_address: str = None):
        self.token_address = utils.normalize_address_eip55(token_address)
        self.partner_address = utils.normalize_address_eip55(partner_address)

    @property
    def name(self) -> str:
        return "pending-transfers"

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

    def from_dict(self, response: Dict[str, Any]) -> None:
        self.pending_transfers = response

    def to_dict(self) -> Dict[str, Any]:
        return {"pending_transfers": self.pending_transfers}
