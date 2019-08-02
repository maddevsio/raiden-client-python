import json
from argparse import ArgumentParser, Namespace, _SubParsersAction
from typing import Any, Dict

from raiden_client.plugins import BasePlugin


class ConnectionsPlugin(BasePlugin):
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

    def parse_response(self, response) -> Dict[str, Any]:
        self.connections = response

    def to_dict(self):
        return {"connections": self.connections}

    @classmethod
    def configure_parser(cls, arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
        connections = subparser.add_parser("connections", help="Query details of all joined token networks")
        connections.set_defaults(func=cls.plugin_execute)

    @classmethod
    def plugin_execute(cls, args: Namespace) -> None:
        plugin = cls()
        output = plugin.raiden_node_api_interact(args.endpoint)
        print(json.dumps(output, indent=2))
