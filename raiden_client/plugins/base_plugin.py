from abc import ABC, abstractclassmethod, abstractmethod
from argparse import ArgumentParser, _SubParsersAction
from typing import Any, Dict

import requests
from web3 import Web3

from raiden_client.exceptions import ResponseStatusCodeException


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

    @abstractmethod
    def payload(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def parse_response(self, response: Dict[str, Any]) -> None:
        raise NotImplementedError()

    @classmethod
    @abstractclassmethod
    def configure_parser(cls, arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
        raise NotImplementedError()

    @classmethod
    def validate_status_code(cls, status_code: int, text: str) -> int:
        if status_code not in [200, 201]:
            raise ResponseStatusCodeException(f"HTTP {status_code}: {text}")
        return status_code

    def url(self, host: str) -> str:
        return f"{host}api/{self.version}{self.endpoint}"

    def raiden_node_api_interact(self, host: str) -> Dict[str, Any]:
        resp = requests.request(method=self.method, url=self.url(host), json=self.payload())
        self.validate_status_code(resp.status_code, resp.text)
        return self.parse_response(resp.json())

    def _normalize_address(self, address: str) -> str:
        """Normalize address to EIP55 standard."""
        return Web3.toChecksumAddress(address)
