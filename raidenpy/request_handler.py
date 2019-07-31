import requests

from raidenpy.endpoints import BaseRequest, BaseResponse


class Request:
    def __init__(self, endpoint: str, version: str = "v1") -> None:
        self.endpoint = f"{endpoint}/api/{version}"

    def do(self, request: BaseRequest) -> BaseResponse:
        """Send HTTP request to URI within defined method."""
        return requests.request(method=request.method, url=f"{self.endpoint}{request.endpoint}")
