from typing import Any, Dict

from raiden_client.endpoints import BaseRequest, BaseResponse
from raiden_client.types import Address, ConnectionType


class ConnectionsRequest(BaseRequest):
    """Query details of all joined token networks

    GET /api/(version)/connections
    https://raiden-network.readthedocs.io/en/latest/rest_api.html#get--api-(version)-connections
    """

    @property
    def endpoint(self) -> str:
        return "/connections"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}


class ConnectionsResponse(BaseResponse):
    def __init__(self, connections: Dict[Address, ConnectionType]):
        self.connections = connections

    def to_dict(self) -> Dict[str, Dict[Address, ConnectionType]]:
        return {"connections": self.connections}

    @classmethod
    def from_dict(cls, d: Dict[str, Dict[Address, ConnectionType]]) -> BaseResponse:
        return cls(connections=d["connections"])
