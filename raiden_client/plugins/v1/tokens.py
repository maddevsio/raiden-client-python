import json
from typing import Dict, Any
from argparse import ArgumentParser, _SubParsersAction, Namespace
from raiden_client.plugins import BasePlugin


class TokensPlugin(BasePlugin):
    """Registers a token.
    If a token is not registered yet (i.e.: A token network for that token does not exist in the registry),
    we need to register it by deploying a token network contract for that token.

    PUT /api/(version)/tokens/(token_address)
    Doc: https://raiden-network.readthedocs.io/en/latest/rest_api.html#deploying
    """
    tokens = None

    def __init__(self, token_address: str = None) -> None:
        if token_address:
            token_address = self._normalize_address(token_address)
        self.token_address = token_address

    @property
    def name(self) -> str:
        return "tokens"

    @property
    def endpoint(self) -> str:
        if self.token_address:
            return f"/tokens/{self.token_address}"
        return "/tokens"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}

    def parse_response(self, response) -> Dict[str, Any]:
        self.tokens = response

    def to_dict(self):
        return {"tokens": self.tokens}

    @classmethod
    def configure_parser(cls, arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
        tokens = subparser.add_parser("tokens", help="Query list of registered tokens")
        tokens.add_argument("-t", "--token-address", required=False, help="For the given token address")
        tokens.set_defaults(func=cls.plugin_execute)

    @classmethod
    def plugin_execute(cls, args: Namespace) -> None:
        plugin = cls(args.token_address)
        output = plugin.raiden_node_api_interact(args.endpoint)
        print(json.dumps(output, indent=2))
