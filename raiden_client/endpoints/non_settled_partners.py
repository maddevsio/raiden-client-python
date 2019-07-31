from typing import Any, Dict, List

from raiden_client.endpoints import BaseRequest, BaseResponse
from raiden_client.types import Address, NonSettledPartners


class NonSettledPartnersRequest(BaseRequest):
    """Returns a list of all partners with whom you have non-settled channels for a certain token.

    GET /api/(version)/tokens/(token_address)/partners
    """

    def __init__(self, token_address: Address):
        # TODO: EIP-55 token encode
        self.token_address = token_address

    @property
    def endpoint(self) -> str:
        return f"/tokens/{self.token_address}/partners"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}


class NonSettledPartnersResponse(BaseResponse):
    """Returns a list of all unsettled channels."""

    def __init__(self, non_settled_partners: List[NonSettledPartners]):
        self.non_settled_partners = non_settled_partners

    def to_dict(self) -> Dict[str, List[NonSettledPartners]]:
        return {"non_settled_partners": self.non_settled_partners}

    @classmethod
    def from_dict(cls, d: Dict[str, List[NonSettledPartners]]) -> "NonSettledPartnersResponse":
        return cls(non_settled_partners=d["non_settled_partners"])
