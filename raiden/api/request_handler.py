from typing import Dict

import requests

from raiden.exceptions import ResponseStatusCodeException


def verify_status_code(status_code):
    if status_code == 404:
        raise ResponseStatusCodeException()
    return status_code


class Request:
    def __init__(self, endpoint: str, version: str = "v1") -> None:
        self.endpoint = f"{endpoint}/api/{version}"

    def get(self, uri: str) -> Dict[str, str]:
        url = "".join([self.endpoint, uri])
        response = requests.get(url)
        verify_status_code(response.status_code)
        return response.json()

    def put(self, uri: str, payload: Dict = None) -> Dict[str, str]:
        if not payload:
            payload = {}

        response = requests.put(
            "".join([self.endpoint, uri]),
            headers={'Content-Type': 'application/json'},
            json=payload
        )
        verify_status_code(response.status_code)
        return response.json()
