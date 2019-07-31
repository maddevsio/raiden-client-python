from typing import Any, Dict

from raiden_client.endpoints import BaseRequest, BaseResponse
from raiden_client.types import Address, PaymentType


class PaymentRequest(BaseRequest):
    """Initiate a payment.
    Args:
        - amount (int) – Amount to be sent to the target
        - identifier (int) – Identifier of the payment (optional)

    POST /api/(version)/payments/(token_address)/(target_address)
    https://raiden-network.readthedocs.io/en/latest/rest_api.html#payments
    """

    def __init__(self, token_address: Address, target_address: Address, amount: int, identifier: int = None) -> None:
        # TODO: adop regarding API doc
        self.token_address = token_address
        self.target_address = target_address
        self.amount = amount
        self.identifier = identifier

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


class PaymentResponse(BaseResponse):
    def __init__(self, payment: PaymentType):
        self.payment = payment

    def to_dict(self) -> Dict[str, PaymentType]:
        return {"payment": self.payment}

    @classmethod
    def from_dict(cls, d: Dict[str, Dict[Address, PaymentType]]) -> BaseResponse:
        return cls(payment=d["payment"])
