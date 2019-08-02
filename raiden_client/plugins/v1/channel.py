import json
from argparse import ArgumentParser, Namespace, _SubParsersAction
from typing import Any, Dict

from raiden_client.plugins import BasePlugin


class ChannelPlugin(BasePlugin):
    """Query information about one of your channels.

    The channel is specified by the address of the token and the partner’s address.

    GET /api/(version)/channels/(token_address)/(partner_address)
    """

    channel = None

    def __init__(self, token_address: str, partner_address: str) -> None:
        self.token_address = self._normalize_address(token_address)
        self.partner_address = self._normalize_address(partner_address)

    @property
    def name(self) -> str:
        return "channel"

    @property
    def endpoint(self) -> str:
        return f"/channels/{self.token_address}/{self.partner_address}"

    @property
    def method(self) -> str:
        return "get"

    @classmethod
    def payload(cls) -> Dict[str, Any]:
        return {}

    def parse_response(self, response) -> Dict[str, Any]:
        self.channel = response

    def to_dict(self):
        return {"channel": self.channel}

    @classmethod
    def configure_parser(cls, arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
        channel = subparser.add_parser("channel", help="Request a channel detail")
        channel.add_argument("-t", "--token-address", required=True, help="For the given token address")
        channel.add_argument("-p", "--partner-address", required=True, help="For the given partner address")
        channel.set_defaults(func=cls.plugin_execute)

    @classmethod
    def plugin_execute(cls, args: Namespace) -> None:
        plugin = cls(args.token_address, args.partner_address)
        output = plugin.raiden_node_api_interact(args.endpoint)
        print(json.dumps(output, indent=2))
