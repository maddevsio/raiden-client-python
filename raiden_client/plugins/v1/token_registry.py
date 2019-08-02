import json
from argparse import ArgumentParser, Namespace, _SubParsersAction
from typing import Any, Dict

from raiden_client.plugins import BasePlugin


class TokenRegisterPlugin(BasePlugin):
    """Registers a token.
    If a token is not registered yet (i.e.: A token network for that token does not exist in the registry),
    we need to register it by deploying a token network contract for that token.

    PUT /api/(version)/tokens/(token_address)
    Doc: https://raiden-network.readthedocs.io/en/latest/rest_api.html#deploying
    """

    token_network_address = None

    def __init__(self, token_address: str = None) -> None:
        self.token_address = self._normalize_address(token_address)

    @property
    def name(self) -> str:
        return "token-register"

    @property
    def endpoint(self) -> str:
        return f"/tokens/{self.token_address}"

    @property
    def method(self) -> str:
        return "put"

    def payload(self) -> Dict[str, Any]:
        return {}

    def parse_response(self, response) -> Dict[str, Any]:
        self.token_network_address = response

    def to_dict(self):
        return {"token_network_address": self.token_network_address}

    @classmethod
    def configure_parser(cls, arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
        register_token = subparser.add_parser("token-register", help="Registering a token by token address")
        register_token.add_argument("-t", "--token-address", required=True, help="Token address")
        register_token.set_defaults(func=cls.plugin_execute)

    @classmethod
    def plugin_execute(cls, args: Namespace) -> None:
        plugin = cls(args.token_address)
        output = plugin.raiden_node_api_interact(args.endpoint)
        print(json.dumps(output, indent=2))
