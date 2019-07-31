from typing import Any, Dict

from raiden_client.endpoints import BaseRequest, BaseResponse
from raiden_client.types import Address, ConnectionType


class ConnectionDisconnectRequest(BaseRequest):
    """Leave a token network.

    PUT /api/(version)/connections/(token_address)
    """

    def __init__(self, token_address: Address) -> None:
        # TODO: adop regarding API doc
        self.token_address = token_address

    @property
    def endpoint(self) -> str:
        return f"/connections/{self.token_address}"

    @property
    def method(self) -> str:
        return "delete"

    def payload(self) -> Dict[str, Any]:
        return {}


class ConnectionDisconnectResponse(BaseResponse):
    def __init__(self, connection: Dict[Address, ConnectionType]):
        self.connection = connection

    def to_dict(self) -> Dict[str, Dict[Address, ConnectionType]]:
        return {"connection": self.connection}

    @classmethod
    def from_dict(cls, d: Dict[str, Dict[Address, ConnectionType]]) -> BaseResponse:
        return cls(connection=d["connection"])
