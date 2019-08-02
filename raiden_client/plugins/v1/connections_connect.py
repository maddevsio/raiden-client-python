import json
from argparse import ArgumentParser, Namespace, _SubParsersAction
from typing import Any, Dict

from raiden_client.plugins import BasePlugin


class ConnectPlugin(BasePlugin):
    """Automatically join a token network.

    PUT /api/(version)/connections/(token_address)
    """

    connection = None

    def __init__(
        self, token_address: str, funds: int, initial_channel_target: int = None, joinable_funds_target: float = None
    ) -> None:
        self.token_address = self._normalize_address(token_address)
        self.funds = funds
        self.initial_channel_target = initial_channel_target
        self.joinable_funds_target = joinable_funds_target

    @property
    def name(self) -> str:
        return "connect"

    @property
    def endpoint(self) -> str:
        return f"/connections/{self.token_address}"

    @property
    def method(self) -> str:
        return "put"

    def payload(self) -> Dict[str, Any]:
        payload = {"funds": self.funds}

        if self.initial_channel_target:
            payload["initial_channel_target"] = self.initial_channel_target

        if self.joinable_funds_target:
            payload["joinable_funds_target"] = self.joinable_funds_target
        return payload

    def parse_response(self, response) -> Dict[str, Any]:
        self.connection = response

    def to_dict(self):
        return {"connection": self.connection}

    @classmethod
    def configure_parser(cls, arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
        connect = subparser.add_parser("connect", help="Automatically join a token network")
        connect.add_argument("-t", "--token-address", required=True, help="Token address")
        connect.add_argument("--funds", required=True, help="Token address")
        connect.add_argument("--initial-channel-target", required=False, help="Token address")
        connect.add_argument("--joinable-funds-target", type=float, required=False, help="Token address")
        connect.set_defaults(func=cls.plugin_execute)

    @classmethod
    def plugin_execute(cls, args: Namespace) -> None:
        plugin = cls(
            token_address=args.token_address,
            funds=args.funds,
            initial_channel_target=args.initial_channel_target,
            joinable_funds_target=args.joinable_funds_target,
        )
        output = plugin.raiden_node_api_interact(args.endpoint)
        print(json.dumps(output, indent=2))
