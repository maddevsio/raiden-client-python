from typing import Any, Dict

from raiden_client import utils
from raiden_client.endpoints import BaseEndpoint


class NonSettledPartners(BaseEndpoint):
    """Returns a list of all partners with whom you have non-settled channels for a certain token.

    GET /api/(version)/tokens/(token_address)/partners
    """
    non_settled_partners = None

    def __init__(self, token_address: str) -> None:
        self.token_address = utils.normalize_address_eip55(token_address)

    @property
    def name(self) -> str:
        return "non-settled"

    @property
    def endpoint(self) -> str:
        return f"/tokens/{self.token_address}/partners"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}

    def from_dict(self, response: Dict[str, Any]) -> None:
        self.non_settled_partners = response

    def to_dict(self) -> Dict[str, Any]:
        return {"non_settled_partners": self.non_settled_partners}
