import json
from argparse import ArgumentParser, Namespace, _SubParsersAction
from typing import Any, Dict

from raiden_client.plugins import BasePlugin


class NonSettledPartnersPlugin(BasePlugin):
    """Returns a list of all partners with whom you have non-settled channels for a certain token.

    GET /api/(version)/tokens/(token_address)/partners
    """

    non_settled_partners = None

    def __init__(self, token_address: str) -> None:
        self.token_address = self._normalize_address(token_address)

    @property
    def name(self) -> str:
        return "non-settled"

    @property
    def endpoint(self) -> str:
        return f"/tokens/{self.token_address}/partners"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}

    def parse_response(self, response) -> Dict[str, Any]:
        self.non_settled_partners = response

    def to_dict(self):
        return {"non_settled_partners": self.non_settled_partners}

    @classmethod
    def configure_parser(cls, arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
        non_settled_partners = subparser.add_parser("non-settled", help="Partners with non-settled channels")
        non_settled_partners.add_argument("-t", "--token-address", required=True, help="For the given token address")
        non_settled_partners.set_defaults(func=cls.plugin_execute)

    @classmethod
    def plugin_execute(cls, args: Namespace) -> None:
        plugin = cls(args.token_address)
        output = plugin.raiden_node_api_interact(args.endpoint)
        print(json.dumps(output, indent=2))
