from typing import Any, Dict

from raiden_client import utils
from raiden_client.endpoints import BaseEndpoint


class MintTokens(BaseEndpoint):
    """Mint tokens

    POST /api/(version)/_testing/tokens/(token_address)/mint
    """
    transaction_hash = None

    def __init__(self, token_address: str, to: str, value: int, contract_method: str = "mintFor"):
        """
        :params: to (address) – The address to assign the minted tokens to.
        :params: value (int) – The amount of tokens to be minted.
        :params: contract_method (string) – The name of the contract’s minting method.
                Must be one of (mintFor/mint/increaseSupply). Defaults to mintFor.
        """
        self.token_address = utils.normalize_address_eip55(token_address)
        self.to = utils.normalize_address_eip55(to)
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

    def from_dict(self, response: Dict[str, Any]) -> None:
        self.transaction_hash = response

    def to_dict(self) -> Dict[str, Any]:
        return {"transaction_hash": self.transaction_hash}
