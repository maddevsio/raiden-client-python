from typing import Any, Dict

from raiden_client.endpoints import BaseEndpoint


class Address(BaseEndpoint):
    """Querying Information About Your Raiden Node

    Raiden address is the same address as the Ethereum
    address chosen, when starting the Raiden node

    GET /api/(version)/address
    https://raiden-network.readthedocs.io/en/latest/rest_api.html#querying-information-about-your-raiden-node
    """
    our_address = None

    @property
    def name(self) -> str:
        return "address"

    @property
    def endpoint(self) -> str:
        return "/address"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}

    def from_dict(self, response: Dict[str, Any]) -> None:
        if "our_address" in response:
            self.our_address = response["our_address"]

    def to_dict(self) -> Dict[str, str]:
        return {"our_address": self.our_address}
