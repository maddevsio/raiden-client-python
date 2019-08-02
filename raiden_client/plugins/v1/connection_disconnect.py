import json
from argparse import ArgumentParser, Namespace, _SubParsersAction
from typing import Any, Dict

from raiden_client.plugins import BasePlugin


class DisconnectPlugin(BasePlugin):
    """Leave a token network.

    DELETE /api/(version)/connections/(token_address)
    """

    connection = None

    def __init__(self, token_address: str) -> None:
        self.token_address = self._normalize_address(token_address)

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

    def parse_response(self, response) -> Dict[str, Any]:
        self.connection = response

    def to_dict(self):
        return {"connection": self.connection}

    @classmethod
    def configure_parser(cls, arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
        connection_disconnect = subparser.add_parser("disconnect", help="Leave a token network")
        connection_disconnect.add_argument("-t", "--token-address", required=True, help="Token address")
        connection_disconnect.set_defaults(func=cls.plugin_execute)

    @classmethod
    def plugin_execute(cls, args: Namespace) -> None:
        plugin = cls(args.token_address)
        output = plugin.raiden_node_api_interact(args.endpoint)
        print(json.dumps(output, indent=2))
