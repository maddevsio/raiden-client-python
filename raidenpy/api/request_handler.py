from typing import Dict

import requests

from raidenpy.exceptions import ResponseStatusCodeException


def verify_status_code(status_code):
    if status_code == 404:
        raise ResponseStatusCodeException()
    return status_code


class Request:
    def __init__(self, endpoint: str, version: str = "v1") -> None:
        self.endpoint = f"{endpoint}/api/{version}"

    def url(self, uri: str) -> str:
        return "".join([self.endpoint, uri])

    def do(self, method: str, uri: str) -> Dict[str, str]:
        """Send HTTP request to URI within defined method.
        """
        response = requests.request(method=method, url=self.url(uri))
        if verify_status_code(response.status_code):
            return response.json()
        raise ResponseStatusCodeException()
