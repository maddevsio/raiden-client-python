import json
from argparse import ArgumentParser, Namespace, _SubParsersAction
from typing import Any, Dict

from raiden_client.plugins import BasePlugin


class MintTokensPlugin(BasePlugin):
    """Mint tokens
    Args:
        - to (address) – The address to assign the minted tokens to.
        - value (int) – The amount of tokens to be minted.
        - contract_method (string) – The name of the contract’s minting method.
            Must be one of (mintFor/mint/increaseSupply). Defaults to mintFor.

    POST /api/(version)/_testing/tokens/(token_address)/mint
    """

    transaction_hash = None

    def __init__(self, token_address: str, to: str, value: int, contract_method: str = "mintFor"):
        self.token_address = self._normalize_address(token_address)
        self.to = self._normalize_address(to)
        self.value = value
        self.contract_method = contract_method

    @property
    def name(self) -> str:
        return "mint-tokens"

    @property
    def endpoint(self) -> str:
        return f"/_testing/tokens/{self.token_address}/mint"

    @property
    def method(self) -> str:
        return "post"

    def payload(self) -> Dict[str, Any]:
        return {"to": self.to, "value": self.value, "contract_method": self.contract_method}

    def parse_response(self, response) -> Dict[str, Any]:
        self.transaction_hash = response

    def to_dict(self):
        return {"transaction_hash": self.transaction_hash}

    @classmethod
    def configure_parser(cls, arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
        mint_tokens = subparser.add_parser("mint-token", help="API endpoints for testing")
        mint_tokens.add_argument("-t", "--token-address", required=True, help="Target address")
        mint_tokens.add_argument("--to", required=True, help="The address to assign the minted tokens to")
        mint_tokens.add_argument("--value", required=True, help="he amount of tokens to be minted")
        mint_tokens.add_argument("--contract-method", required=False, help="The name of the contract’s minting method")
        mint_tokens.set_defaults(func=cls.plugin_execute)

    @classmethod
    def plugin_execute(cls, args: Namespace) -> None:
        plugin = cls(
            token_address=args.token_address, to=args.to, value=args.value, contract_method=args.contract_method
        )
        output = plugin.raiden_node_api_interact(args.endpoint)
        print(json.dumps(output, indent=2))
