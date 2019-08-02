import json
from argparse import ArgumentParser, Namespace, _SubParsersAction
from typing import Any, Dict

from raiden_client.plugins import BasePlugin


class PaymentPlugin(BasePlugin):
    """Initiate a payment.
    Args:
        - amount (int) – Amount to be sent to the target
        - identifier (int) (optional) – Identifier of the payment

    POST /api/(version)/payments/(token_address)/(target_address)
    https://raiden-network.readthedocs.io/en/latest/rest_api.html#payments
    """

    payment = None

    def __init__(self, token_address: str, target_address: str, amount: int, identifier: int = None) -> None:
        self.token_address = self._normalize_address(token_address)
        self.target_address = self._normalize_address(target_address)
        self.amount = amount
        self.identifier = identifier

    @property
    def name(self) -> str:
        return "payment"

    @property
    def endpoint(self) -> str:
        return f"/payments/{self.token_address}/{self.target_address}"

    @property
    def method(self) -> str:
        return "post"

    def payload(self) -> Dict[str, Any]:
        data = {"amount": self.amount}
        if self.identifier:
            data["identifier"] = self.identifier
        return data

    def parse_response(self, response) -> Dict[str, Any]:
        self.payment = response

    def to_dict(self):
        return {"payment": self.payment}

    @classmethod
    def configure_parser(cls, arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
        payment = subparser.add_parser("payment", help="Initiate a payment")
        payment.add_argument("-t", "--token-address", required=True, help="Token address")
        payment.add_argument("--target-address", required=True, help="Target address")
        payment.add_argument("--amount", required=True, help="Token address")
        payment.add_argument("--identifier", required=False, help="Token address")
        payment.set_defaults(func=cls.plugin_execute)

    @classmethod
    def plugin_execute(cls, args: Namespace) -> None:
        plugin = cls(
            token_address=args.token_address,
            target_address=args.target_address,
            amount=args.amount,
            identifier=args.identifier,
        )
        output = plugin.raiden_node_api_interact(args.endpoint)
        print(json.dumps(output, indent=2))
