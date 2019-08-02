import json
from argparse import ArgumentParser, Namespace, _SubParsersAction
from typing import Any, Dict

from raiden_client.plugins import BasePlugin


class ChannelClose(BasePlugin):
    """Close a channel.

    PATCH /api/(version)/channels/(token_address)/(partner_address)
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
        return "patch"

    def payload(self) -> Dict[str, Any]:
        return {"state": "closed"}

    def parse_response(self, response) -> Dict[str, Any]:
        self.channel = response

    def to_dict(self):
        return {"channel": self.channel}

    @classmethod
    def configure_parser(cls, arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
        channel_close = subparser.add_parser("channel-close", help="Close a channell")
        channel_close.add_argument("-t", "--token-address", required=True, help="The token we want to be used")
        channel_close.add_argument("-p", "--partner-address", required=True, help="Channel partner address")
        channel_close.set_defaults(func=cls.plugin_execute)

    @classmethod
    def plugin_execute(cls, args: Namespace) -> None:
        plugin = cls(args.token_address, args.partner_address)
        output = plugin.raiden_node_api_interact(args.endpoint)
        print(json.dumps(output, indent=2))
