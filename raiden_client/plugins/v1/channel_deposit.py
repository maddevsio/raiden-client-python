import json
from argparse import ArgumentParser, Namespace, _SubParsersAction
from typing import Any, Dict

from raiden_client.plugins import BasePlugin


class ChannelDepositPlugin(BasePlugin):
    """Increase the deposit in channel.

    PATCH /api/(version)/channels/(token_address)/(partner_address)
    """

    channel = None

    def __init__(self, token_address: str, partner_address: str, total_deposit: int) -> None:
        self.token_address = self._normalize_address(token_address)
        self.partner_address = self._normalize_address(partner_address)
        self.total_deposit = total_deposit

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
        return {"total_deposit": self.total_deposit}

    def parse_response(self, response) -> Dict[str, Any]:
        self.channel = response

    def to_dict(self):
        return {"channel": self.channel}

    @classmethod
    def configure_parser(cls, arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
        channel_deposit = subparser.add_parser("deposit-increase", help="Increase channel deposit")
        channel_deposit.add_argument("-t", "--token-address", required=True, help="For the given token address")
        channel_deposit.add_argument("-p", "--partner-address", required=True, help="Channel partner address")
        channel_deposit.add_argument("--total-deposit", required=True, help="The increased total deposit")
        channel_deposit.set_defaults(func=cls.plugin_execute)

    @classmethod
    def plugin_execute(cls, args: Namespace) -> None:
        plugin = cls(
            token_address=args.token_address, partner_address=args.partner_address, total_deposit=args.total_deposit
        )
        output = plugin.raiden_node_api_interact(args.endpoint)
        print(json.dumps(output, indent=2))
