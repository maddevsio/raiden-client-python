from typing import Any, Dict

from raiden_client.endpoints import BaseRequest, BaseResponse
from raiden_client.types import Address, ConnectionType


class ConnectionConnectRequest(BaseRequest):
    """Automatically join a token network.

    PUT /api/(version)/connections/(token_address)
    """

    def __init__(
        self,
        token_address: Address,
        funds: int,
        initial_channel_target: int = None,
        joinable_funds_target: float = None,
    ) -> None:
        # TODO: adop regarding API doc
        self.token_address = token_address
        self.funds = funds
        self.initial_channel_target = initial_channel_target
        self.joinable_funds_target = joinable_funds_target

    @property
    def endpoint(self) -> str:
        return f"/connections/{self.token_address}"

    @property
    def method(self) -> str:
        return "put"

    def payload(self) -> Dict[str, Any]:
        payload = {"funds": self.funds}

        if self.initial_channel_target:
            payload["initial_channel_target"] = self.initial_channel_target

        if self.joinable_funds_target:
            payload["joinable_funds_target"] = self.joinable_funds_target
        return payload


class ConnectionConnectResponse(BaseResponse):
    def __init__(self, connection: Dict[Address, ConnectionType]):
        self.connection = connection

    def to_dict(self) -> Dict[str, Dict[Address, ConnectionType]]:
        print(self.connection)
        return {"connection": self.connection}

    @classmethod
    def from_dict(cls, d: Dict[str, Dict[Address, ConnectionType]]) -> BaseResponse:
        return cls(connection=d["connection"])
