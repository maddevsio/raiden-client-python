from typing import Any, Dict

from raiden_client import utils
from raiden_client.endpoints.v1 import BaseV1Endpoint


class Payment(BaseV1Endpoint):
    """Initiate a payment.

    POST /api/(version)/payments/(token_address)/(target_address)
    https://raiden-network.readthedocs.io/en/latest/rest_api.html#payments
    """
    payment = None

    def __init__(self, token_address: str, target_address: str, amount: int, identifier: int = None) -> None:
        """
        :params: amount (int) – Amount to be sent to the target
        :params: identifier (int) (optional) – Identifier of the payment
        """
        self.token_address = utils.normalize_address_eip55(token_address)
        self.target_address = utils.normalize_address_eip55(target_address)
        self.amount = amount
        self.identifier = identifier

    @property
    def name(self) -> str:
        return "payment"

    @property
    def endpoint(self) -> str:
        return f"/payments/{self.token_address}/{self.target_address}"

    @property
    def method(self) -> str:
        return "post"

    def payload(self) -> Dict[str, Any]:
        data = {"amount": self.amount}
        if self.identifier:
            data["identifier"] = self.identifier
        return data

    def from_dict(self, response: Dict[str, Any]) -> None:
        self.payment = response

    def to_dict(self) -> Dict[str, Any]:
        return {"payment": self.payment}
