import json
from argparse import ArgumentParser, Namespace, _SubParsersAction
from typing import Any, Dict

from raiden_client.plugins import BasePlugin


class PendingTransfersPlugin(BasePlugin):
    """Returns a list of all transfers that have not been completed yet.

    GET /api/(version)/pending_transfers
    GET /api/(version)/pending_transfers/(token_address)
    GET /api/(version)/pending_transfers/(token_address)/(partner_address)
    """

    pending_transfers = None

    def __init__(self, token_address: str = None, partner_address: str = None):
        if token_address:
            token_address = self._normalize_address(token_address)

        if partner_address:
            partner_address = self._normalize_address(partner_address)

        self.token_address = token_address
        self.partner_address = partner_address

    @property
    def name(self) -> str:
        return "pending-transfers"

    @property
    def endpoint(self) -> str:
        if self.token_address and self.partner_address:
            return f"/pending_transfers/{self.token_address}/{self.partner_address}"

        if self.token_address:
            return f"/pending_transfers/{self.token_address}"

        return "/pending_transfers"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}

    def parse_response(self, response) -> Dict[str, Any]:
        self.pending_transfers = response

    def to_dict(self):
        return {"pending_transfers": self.pending_transfers}

    @classmethod
    def configure_parser(cls, arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
        pending_transfers = subparser.add_parser("pending-transfers", help="List of uncompleted transfers")
        pending_transfers.add_argument("-t", "--token-address", required=True, help="For the given token address")
        pending_transfers.add_argument("-p", "--partner-address", required=True, help="For the given partner address")
        pending_transfers.set_defaults(func=cls.plugin_execute)

    @classmethod
    def plugin_execute(cls, args: Namespace) -> None:
        plugin = cls(token_address=args.token_address, partner_address=args.partner_address)
        output = plugin.raiden_node_api_interact(args.endpoint)
        print(json.dumps(output, indent=2))
