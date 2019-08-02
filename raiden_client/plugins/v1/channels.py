import json
from argparse import ArgumentParser, Namespace, _SubParsersAction
from typing import Any, Dict

from raiden_client.plugins import BasePlugin


class ChannelsPlugin(BasePlugin):
    """Request a list of all unsettled channels.

    GET /api/(version)/channels

    All channels for the given token address
    GET /api/(version)/channels/(token_address)
    """

    channels = None

    def __init__(self, token_address: str = None) -> None:
        if token_address:
            self.token_address = self._normalize_address(token_address)
        self.token_address = token_address

    @property
    def name(self) -> str:
        return "channels"

    @property
    def endpoint(self) -> str:
        if self.token_address:
            return f"/channels/{self.token_address}"
        return "/channels"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}

    def parse_response(self, response) -> Dict[str, Any]:
        self.channels = response

    def to_dict(self):
        return {"channels": self.channels}

    @classmethod
    def configure_parser(cls, arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
        channels = subparser.add_parser("channels", help="Request a list of all unsettled channels")
        channels.add_argument("-t", "--token-address", required=False, help="For the given token address")
        channels.set_defaults(func=cls.plugin_execute)

    @classmethod
    def plugin_execute(cls, args: Namespace) -> None:
        plugin = cls(args.token_address)
        output = plugin.raiden_node_api_interact(args.endpoint)
        print(json.dumps(output, indent=2))
