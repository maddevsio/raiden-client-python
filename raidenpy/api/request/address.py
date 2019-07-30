from requests import Request
from typing import Dict, Any
from raidenpy.api.request import BaseRequest, BaseResponse


class AddressRequest(BaseRequest):
    """Raiden address is the same address as the Ethereum
    address chosen, when starting the Raiden node
    """

    @property
    def endpoint(self) -> str:
        return "/address"

    @property
    def method(self) -> str:
        return "get"

    def payload(self) -> Dict[str, Any]:
        return {}


class AddressResponse(BaseResponse):

    def __init__(self, response: Request):
        self.response = response

    def validate_status_code(self, status_code: int) -> bool:
        if status_code != 200:
            raise Exception()
        return True

    def to_dict(self) -> Dict[str, str]:
        self.validate_status_code(self.response.status_code)
        return self.response.json()
