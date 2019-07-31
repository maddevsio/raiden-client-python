from typing import Any, Dict, List

from raiden_client.endpoints import BaseRequest, BaseResponse
from raiden_client.types import Address, PaymentEvent


class PaymentEventsRequest(BaseRequest):
    """Querying payment events.

    GET /api/v1/payments/(token_address)/(target_address)
    https://raiden-network.readthedocs.io/en/latest/rest_api.html#querying-events
    """

    def __init__(self, token_address: Address, target_address: Address) -> None:
        # TODO: adop regarding API doc
        self.token_address = token_address
        self.target_address = target_address

    @property
    def endpoint(self) -> str:
        return f"/payments/{self.token_address}/{self.target_address}"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}


class PaymentEventsResponse(BaseResponse):
    def __init__(self, payment_events: List[PaymentEvent]):
        self.payment_events = payment_events

    def to_dict(self) -> Dict[str, List[PaymentEvent]]:
        return {"payment_events": self.payment_events}

    @classmethod
    def from_dict(cls, d: Dict[str, List[PaymentEvent]]) -> BaseResponse:
        return cls(payment_events=d["payment_events"])
