from typing import Any, Dict

from raiden_client import utils
from raiden_client.endpoints import BaseEndpoint


class Disconnect(BaseEndpoint):
    """Leave a token network.

    DELETE /api/(version)/connections/(token_address)
    """

    connection = None

    def __init__(self, token_address: str) -> None:
        self.token_address = utils.normalize_address_eip55(token_address)

    @property
    def name(self) -> str:
        return "disconnect"

    @property
    def endpoint(self) -> str:
        return f"/connections/{self.token_address}"

    @property
    def method(self) -> str:
        return "delete"

    def payload(self) -> Dict[str, Any]:
        return {}

    def from_dict(self, response: Dict[str, Any]) -> None:
        self.connection = response

    def to_dict(self) -> Dict[str, Any]:
        return {"connection": self.connection}
