from typing import Any, Dict

import requests

from raiden_client.endpoints import BaseRequest
from raiden_client.exceptions import ResponseStatusCodeException


class APIHandler:
    def __init__(self, endpoint: str, version: str = "v1") -> None:
        self.endpoint = endpoint
        self.version = version

    def validate_status_code(self, status_code: int, text: str) -> int:
        if status_code not in [200, 201]:
            raise ResponseStatusCodeException(f"HTTP {status_code}: {text}")
        return status_code

    def url(self, uri):
        return f"{self.endpoint}/api/{self.version}{uri}"

    def do(self, req: BaseRequest) -> Dict[str, Any]:
        """Send HTTP request to URI within defined method."""
        resp = requests.request(method=req.method, url=self.url(req.endpoint), headers={})
        self.validate_status_code(resp.status_code, resp.text)
        return resp.json()
