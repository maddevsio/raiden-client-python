import requests

from raiden import utils


class Request:
    def __init__(self, endpoint: str, version: str = "v1") -> None:
        self.endpoint = f"{endpoint}/api/{version}"

    def get(self, uri: str) -> str:
        url = "".join([self.endpoint, uri])
        response = requests.get(url)
        return response.json()


class Client:
    """API client.

    Communicate with API via client class.
    """

    def __init__(self, endpoint: str, version: str = "v1") -> None:
        self.request = Request(endpoint, version)

    @property
    def address(self) -> str:
        """Get node address.

        Query your address. When raiden starts, you choose an ethereum address which will also be your raiden address.
        """
        data = self.request.get("/address")
        return data["our_address"]

    def deploy(self, token_address: str) -> str:
        """Registers a token.

        If a token is not registered yet (i.e.: A token network for that token does not exist in the registry),
        we need to register it by deploying a token network contract for that token.
        """
        if not utils.validate_address(token_address):
            raise Exception("Wrong ETH address")

        return token_address
