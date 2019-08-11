from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseEndpoint(ABC):
    version = "v1"

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError()

    @property
    @abstractmethod
    def endpoint(self) -> str:
        raise NotImplementedError()

    @property
    @abstractmethod
    def method(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def payload(self) -> Dict[str, Any]:
        raise NotImplementedError()

    @abstractmethod
    def from_dict(self, response: Dict[str, Any]) -> None:
        raise NotImplementedError()

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        raise NotImplementedError()
