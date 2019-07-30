from typing import List

from raiden import utils
from raiden.api.request_handler import Request
from raiden.types import Address


class Client:
    """API client.
    Communicate with API via client class.
    """

    def __init__(self, endpoint: str, version: str = "v1") -> None:
        self.request = Request(endpoint, version)

    @property
    def address(self) -> Address:
        """Get node address.

        Query your address. When raiden starts, you choose an ethereum address which will also be your raiden address.
        """
        data = self.request.get("/address")
        return Address(utils.decode_hex(data["our_address"]))

    @property
    def tokens(self) -> List[Address]:
        """Checking if a token is already registered."""
        data = self.request.get("/tokens")
        return [Address(utils.decode_hex(item)) for item in data]

    def register_token(self, token_address: str) -> Address:
        """Registering a token by token address"""
        if not utils.validate_address(token_address):
            raise Exception("Wrong ETH address")
        data = self.request.put(f"/tokens/{token_address}")
        return Address(data["token_network_address"])
