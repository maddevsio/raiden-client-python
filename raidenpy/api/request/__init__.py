import abc
from typing import Any, Dict


class BaseRequest(abc.ABC):
    @abc.abstractmethod
    def endpoint(self) -> str:
        raise NotImplementedError()

    @abc.abstractmethod
    def method(self) -> str:
        raise NotImplementedError()

    def payload(self) -> Dict[str, Any]:
        raise NotImplementedError()


class BaseResponse(abc.ABC):
    @abc.abstractmethod
    def validate_status_code(self, status_code: int) -> bool:
        raise NotImplementedError()

    @abc.abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        raise NotImplementedError()
