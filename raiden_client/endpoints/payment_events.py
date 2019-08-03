from typing import Any, Dict

from raiden_client import utils
from raiden_client.endpoints import BaseEndpoint


class PaymentEvents(BaseEndpoint):
    """Querying payment events.

    GET /api/v1/payments/(token_address)/(target_address)
    https://raiden-network.readthedocs.io/en/latest/rest_api.html#querying-events
    """
    payment_events = None

    def __init__(self, token_address: str, target_address: str) -> None:
        self.token_address = utils.normalize_address_eip55(token_address)
        self.target_address = utils.normalize_address_eip55(target_address)

    @property
    def name(self) -> str:
        return "payment-events"

    @property
    def endpoint(self) -> str:
        return f"/payments/{self.token_address}/{self.target_address}"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}

    def from_dict(self, response: Dict[str, Any]) -> None:
        self.payment_events = response

    def to_dict(self) -> Dict[str, Any]:
        return {"payment_events": self.payment_events}
