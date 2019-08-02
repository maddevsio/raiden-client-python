import json
from typing import Dict, Any
from argparse import ArgumentParser, _SubParsersAction, Namespace
from raiden_client.plugins import BasePlugin


class AddressPlugin(BasePlugin):
    """Querying Information About Your Raiden Node

    Raiden address is the same address as the Ethereum
    address chosen, when starting the Raiden node

    GET /api/(version)/address
    https://raiden-network.readthedocs.io/en/latest/rest_api.html#querying-information-about-your-raiden-node
    """
    our_address = None

    @property
    def name(self) -> str:
        return "address"

    @property
    def endpoint(self) -> str:
        return "/address"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}

    def parse_response(self, response) -> Dict[str, Any]:
        self.our_address = response

    def to_dict(self):
        return {
            "our_address": self.our_address
        }

    @classmethod
    def configure_parser(cls, arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
        address = subparser.add_parser("address", help="Query node address")
        address.set_defaults(func=cls.address_func)

    @classmethod
    def address_func(cls, args: Namespace) -> None:
        plugin = cls()
        output = plugin.raiden_node_api_interact(args.endpoint)
        print(json.dumps(output, indent=2))
