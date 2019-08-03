import json
from argparse import ArgumentParser, Namespace, _SubParsersAction
from typing import Any, Dict, List

from raiden_client.plugins import BasePlugin


class TokensPlugin(BasePlugin):
    """Returns a list of addresses of all registered tokens.

    GET /api/(version)/tokens
    https://raiden-network.readthedocs.io/en/latest/rest_api.html#get--api-(version)-tokens

    GET /api/(version)/tokens/(token_address)
    https://raiden-network.readthedocs.io/en/latest/rest_api.html#get--api-(version)-tokens-(token_address)
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

    def parse_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        self.tokens = response

    def to_dict(self) -> Dict[str, List[str]]:
        return {"tokens": self.tokens}

    @classmethod
    def configure_parser(cls, arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
        tokens = subparser.add_parser("tokens", help="Query list of registered tokens")
        tokens.add_argument("-t", "--token-address", required=False, help="For the given token address")
        tokens.set_defaults(func=cls.plugin_execute)

    @classmethod
    def plugin_execute(cls, args: Namespace) -> None:
        plugin = cls(args.token_address)
        plugin.raiden_node_api_interact(args.endpoint)
        output = plugin.to_dict()
        print(json.dumps(output["tokens"], indent=2))
