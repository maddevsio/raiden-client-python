import json
from argparse import ArgumentParser, Namespace, _SubParsersAction
from typing import Any, Dict

from raiden_client.plugins import BasePlugin


class PaymentEventsPlugin(BasePlugin):
    """Querying payment events.

    GET /api/v1/payments/(token_address)/(target_address)
    https://raiden-network.readthedocs.io/en/latest/rest_api.html#querying-events
    """

    payment_events = None

    def __init__(self, token_address: str, target_address: str) -> None:
        self.token_address = self._normalize_address(token_address)
        self.target_address = self._normalize_address(target_address)

    @property
    def name(self) -> str:
        return "payment-events"

    @property
    def endpoint(self) -> str:
        return f"/payments/{self.token_address}/{self.target_address}"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}

    def parse_response(self, response) -> Dict[str, Any]:
        self.payment_events = response

    def to_dict(self):
        return {"payment_events": self.payment_events}

    @classmethod
    def configure_parser(cls, arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
        payment_events = subparser.add_parser("payment-events", help="Querying payment events")
        payment_events.add_argument("-t", "--token-address", required=True, help="Target address")
        payment_events.add_argument("--target-address", required=True, help="Token address")
        payment_events.set_defaults(func=cls.plugin_execute)

    @classmethod
    def plugin_execute(cls, args: Namespace) -> None:
        plugin = cls(token_address=args.token_address, target_address=args.target_address)
        output = plugin.raiden_node_api_interact(args.endpoint)
        print(json.dumps(output, indent=2))
