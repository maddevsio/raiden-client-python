from abc import abstractmethod, abstractclassmethod, ABC
from argparse import ArgumentParser, _SubParsersAction
from typing import Any, Dict
from raiden_client.exceptions import ResponseStatusCodeException
import requests

from web3 import Web3


class BasePlugin(ABC):

    version = "v1"

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def endpoint(self) -> str:
        pass

    @property
    @abstractmethod
    def method(self) -> str:
        pass

    @classmethod
    @abstractmethod
    def payload(cls) -> None:
        pass

    @abstractmethod
    def parse_response(self, response: Any) -> None:
        pass

    @classmethod
    @abstractclassmethod
    def configure_parser(cls, arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
        pass

    @classmethod
    def validate_status_code(cls, status_code: int, text: str) -> int:
        if status_code not in [200, 201]:
            raise ResponseStatusCodeException(f"HTTP {status_code}: {text}")
        return status_code

    def url(self, host) -> str:
        return f"{host}api/{self.version}{self.endpoint}"

    def raiden_node_api_interact(self, host) -> Dict[str, Any]:
        resp = requests.request(
            method=self.method,
            url=self.url(host),
            json=self.payload()
        )
        self.validate_status_code(resp.status_code, resp.text)
        return {"response": resp.json()}

    def _normalize_address(self, address: str) -> str:
        return Web3.toChecksumAddress(address)
