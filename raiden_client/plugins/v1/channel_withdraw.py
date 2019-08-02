import json
from argparse import ArgumentParser, Namespace, _SubParsersAction
from typing import Any, Dict

from raiden_client.plugins import BasePlugin


class ChannelWithdrawPlugin(BasePlugin):
    """Increase the deposit in channel.

    PATCH /api/(version)/channels/(token_address)/(partner_address)
    """

    channel = None

    def __init__(self, token_address: str, partner_address: str, total_withdraw: int) -> None:
        self.token_address = self._normalize_address(token_address)
        self.partner_address = self._normalize_address(partner_address)
        self.total_withdraw = total_withdraw

    @property
    def name(self) -> str:
        return "channel-withdraw"

    @property
    def endpoint(self) -> str:
        return f"/channels/{self.token_address}/{self.partner_address}"

    @property
    def method(self) -> str:
        return "patch"

    def payload(self) -> Dict[str, Any]:
        return {"total_withdraw": self.total_withdraw}

    def parse_response(self, response) -> Dict[str, Any]:
        self.channel = response

    def to_dict(self):
        return {"channel": self.channel}

    @classmethod
    def configure_parser(cls, arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
        channel_withdraw = subparser.add_parser("withdraw-increase", help="Increase channel deposit")
        channel_withdraw.add_argument("-t", "--token-address", required=True, help="For the given token address")
        channel_withdraw.add_argument("-p", "--partner-address", required=True, help="Channel partner address")
        channel_withdraw.add_argument("--total-withdraw", required=True, help="The increased total withdraw")
        channel_withdraw.set_defaults(func=cls.plugin_execute)

    @classmethod
    def plugin_execute(cls, args: Namespace) -> None:
        plugin = cls(
            token_address=args.token_address, partner_address=args.partner_address, total_withdraw=args.total_withdraw
        )
        output = plugin.raiden_node_api_interact(args.endpoint)
        print(json.dumps(output, indent=2))
