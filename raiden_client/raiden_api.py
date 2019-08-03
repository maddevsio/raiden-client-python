import requests
from urllib.parse import urljoin
from typing import Any, Dict

from raiden_client.exceptions import ResponseStatusCodeException
from raiden_client.endpoints.v1 import BaseV1Endpoint


class RaidenAPI:

    def __init__(self, endpoint: str, version: str, plugin: BaseV1Endpoint) -> None:
        self.endpoint = endpoint
        self.version = version
        self.plugin = plugin

    def validate_status_code(self, status_code: int, text: str) -> int:
        if status_code not in [200, 201]:
            raise ResponseStatusCodeException(f"HTTP {status_code}: {text}")
        return status_code

    def url(self) -> str:
        return urljoin(self.endpoint, f"api/{self.version}{self.plugin.endpoint}")

    def request(self) -> Dict[str, Any]:
        resp = requests.request(
            method=self.plugin.method,
            url=self.url(),
            json=self.plugin.payload()
        )
        self.validate_status_code(resp.status_code, resp.text)
        self.plugin.from_dict(resp.json())
        return self.plugin.to_dict()
