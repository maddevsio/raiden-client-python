from typing import Any, Dict

from raiden_client.endpoints import BaseRequest, BaseResponse
from raiden_client.types import Address


class MintTokensRequest(BaseRequest):
    """Mint tokens

    Args:
        - to (address) – The address to assign the minted tokens to.
        - value (int) – The amount of tokens to be minted.
        - contract_method (string) – The name of the contract’s minting method. 
            Must be one of (mintFor/mint/increaseSupply). Defaults to mintFor.

    POST /api/(version)/_testing/tokens/(token_address)/mint
    """

    def __init__(self, token_address: Address, to: Address, value: int, contract_method: str = "mintFor"):
        self.token_address = token_address
        self.to = to
        self.value = value
        # TODO: verify that contract method in [mintFor/mint/increaseSupply]
        self.contract_method = contract_method

    @property
    def endpoint(self) -> str:
        return f"/_testing/tokens/{self.token_address}/mint"

    @property
    def method(self) -> str:
        return "post"

    def payload(self) -> Dict[str, Any]:
        return {"to": self.to, "value": self.value, "contract_method": self.contract_method}


class MintTokensResponse(BaseResponse):
    def __init__(self, transaction_hash: str):
        self.transaction_hash = transaction_hash

    @classmethod
    def from_dict(cls, d: Dict[str, str]) -> BaseResponse:
        return cls(transaction_hash=d["transaction_hash"])

    def to_dict(self) -> Dict[str, str]:
        return {"transaction_hash": self.transaction_hash}
