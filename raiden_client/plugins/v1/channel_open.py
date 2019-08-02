import json
from argparse import ArgumentParser, Namespace, _SubParsersAction
from typing import Any, Dict

from raiden_client.plugins import BasePlugin


class ChannelOpenPlugin(BasePlugin):
    """Opens / creates a channel

    - token_address (address)   – The token we want to be used in the channel.
    - partner_address (address) – The partner we want to open a channel with.
    - total_deposit (int)       – Total amount of tokens to be deposited to the channel
    - settle_timeout (int)      – The amount of blocks that the settle timeout should have.

    PUT /api/(version)/channels
    """

    channel = None

    def __init__(self, token_address: str, partner_address: str, total_deposit: int, settle_timeout: int) -> None:
        self.token_address = self._normalize_address(token_address)
        self.partner_address = self._normalize_address(partner_address)
        self.total_deposit = total_deposit
        self.settle_timeout = settle_timeout

    @property
    def name(self) -> str:
        return "channel-open"

    @property
    def endpoint(self) -> str:
        return f"/channels"

    @property
    def method(self) -> str:
        return "put"

    def payload(self) -> Dict[str, Any]:
        return {
            "token_address": self.token_address,
            "partner_address": self.partner_address,
            "total_deposit": self.total_deposit,
            "settle_timeout": self.settle_timeout,
        }

    def parse_response(self, response) -> Dict[str, Any]:
        self.channel = response

    def to_dict(self):
        return {"channel": self.channel}

    @classmethod
    def configure_parser(cls, arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
        channel_open = subparser.add_parser("channel-open", help="Opens / creates a channel")
        channel_open.add_argument("-t", "--token-address", required=True, help="For the given token address")
        channel_open.add_argument("-p", "--partner-address", required=True, help="Channel partner address")
        channel_open.add_argument("--total-deposit", required=True, help="Amount of tokens to be deposited")
        channel_open.add_argument(
            "--settle-timeout", required=True, help="Amount of blocks that the settle timeout should have"
        )
        channel_open.set_defaults(func=cls.plugin_execute)

    @classmethod
    def plugin_execute(cls, args: Namespace) -> None:
        plugin = cls(
            token_address=args.token_address,
            partner_address=args.partner_address,
            total_deposit=args.total_deposit,
            settle_timeout=args.settle_timeout,
        )
        output = plugin.raiden_node_api_interact(args.endpoint)
        print(json.dumps(output, indent=2))
