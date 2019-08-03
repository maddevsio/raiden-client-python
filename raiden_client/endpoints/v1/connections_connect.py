from typing import Any, Dict

from raiden_client import utils
from raiden_client.endpoints.v1 import BaseV1Endpoint


class Connect(BaseV1Endpoint):
    """Automatically join a token network.

    PUT /api/(version)/connections/(token_address)
    """
    connection = None

    def __init__(self,
                 token_address: str,
                 funds: int,
                 initial_channel_target: int = None,
                 joinable_funds_target: float = None) -> None:
        self.token_address = utils.normalize_address_eip55(token_address)
        self.funds = funds
        self.initial_channel_target = initial_channel_target
        self.joinable_funds_target = joinable_funds_target

    @classmethod
    def name(cls) -> str:
        return "connect"

    @property
    def endpoint(self) -> str:
        return f"/connections/{self.token_address}"

    @property
    def method(self) -> str:
        return "put"

    def payload(self) -> Dict[str, Any]:
        data: Dict[str, Any] = {"funds": self.funds}

        if self.initial_channel_target:
            data["initial_channel_target"] = self.initial_channel_target

        if self.joinable_funds_target:
            data["joinable_funds_target"] = self.joinable_funds_target
        return data

    def from_dict(self, response: Dict[str, Any]) -> None:
        self.connection = response

    def to_dict(self) -> Dict[str, Any]:
        return {"connection": self.connection}
