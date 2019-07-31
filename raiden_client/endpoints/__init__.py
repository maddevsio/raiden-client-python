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
    @classmethod
    @abc.abstractmethod
    def from_dict(cls, d: Dict[str, Any]) -> "BaseResponse":
        raise NotImplementedError()

    @abc.abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        raise NotImplementedError()
