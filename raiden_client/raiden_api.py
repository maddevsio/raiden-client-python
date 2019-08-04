import requests
from urllib.parse import urljoin
from typing import Any, Dict

from raiden_client.endpoints import BaseEndpoint
from raiden_client.exceptions import ResponseStatusCodeException


class RaidenAPI:

    def __init__(self, endpoint: str, version: str) -> None:
        """
        :params: endpoint (str) Raiden node Rest API url
        :params: version (str) Raiden node API version
        """
        self.endpoint = endpoint
        self.version = version

    def validate_status_code(self, status_code: int, text: str) -> int:
        """Validate response status code.

        :params: status_code (int) Response HTTP status code
        :params: text (str) Response text
        :raises: ResponseStatusCodeException
        """
        if status_code not in [200, 201]:
            raise ResponseStatusCodeException(f"HTTP {status_code}: {text}")
        return status_code

    def url(self, uri: str) -> str:
        """Build URL to Raiden API endpoint from uri chunk.

        :params: uri (str) endpoint uri
        :returns: full endpoint url
        """
        return urljoin(self.endpoint, f"api/{self.version}{uri}")

    def request(self, api_endpoint: BaseEndpoint) -> Dict[str, Any]:
        """Send HTTP request to Raiden API

        :params: api_endpoint instance of BaseEndpoint
        :returns: response dictionary
        """
        url = self.url(api_endpoint.endpoint)
        resp = requests.request(
            method=api_endpoint.method,
            url=url,
            json=api_endpoint.payload()
        )
        self.validate_status_code(resp.status_code, resp.text)
        api_endpoint.from_dict(resp.json())
        return api_endpoint.to_dict()
