from typing import Any, Dict

from raiden_client.endpoints.v1 import BaseV1Endpoint


class Connections(BaseV1Endpoint):
    """Query details of all joined token networks

    GET /api/(version)/connections
    https://raiden-network.readthedocs.io/en/latest/rest_api.html#get--api-(version)-connections
    """
    connections = None

    @property
    def name(self) -> str:
        return "connections"

    @property
    def endpoint(self) -> str:
        return "/connections"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}

    def from_dict(self, response: Dict[str, Any]) -> None:
        self.connections = response

    def to_dict(self) -> Dict[str, Any]:
        return {"connections": self.connections}
