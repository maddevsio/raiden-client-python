import requests
from urllib.parse import urljoin
from typing import Any, Dict

from raiden_client.endpoints import BaseEndpoint
from raiden_client.exceptions import ResponseStatusCodeException


class RaidenAPI:

    def __init__(self, endpoint: str, version: str) -> None:
        self.endpoint = endpoint
        self.version = version

    def validate_status_code(self, status_code: int, text: str) -> int:
        if status_code not in [200, 201]:
            raise ResponseStatusCodeException(f"HTTP {status_code}: {text}")
        return status_code

    def url(self, uri: str) -> str:
        return urljoin(self.endpoint, f"api/{self.version}{uri}")

    def request(self, api_endpoint: BaseEndpoint) -> Dict[str, Any]:
        url = self.url(api_endpoint.endpoint)
        resp = requests.request(
            method=api_endpoint.method,
            url=url,
            json=api_endpoint.payload()
        )
        self.validate_status_code(resp.status_code, resp.text)
        api_endpoint.from_dict(resp.json())
        return api_endpoint.to_dict()
