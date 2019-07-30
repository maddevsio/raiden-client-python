from abc import ABC
from typing import List, Any, Dict

from raidenpy.types import Address


class RaidenAPIv1(ABC):
    """Raiden v1 API interface."""

    def address(self) -> Address:
        raise NotImplementedError()

    def tokens(self) -> List[Address]:
        raise NotImplementedError()

    def register_token(self, token_address: str) -> Address:
        raise NotImplementedError()

    def channels(self) -> List[Address]:
        raise NotImplementedError()

    def channels_by_token(self, token_address: str) -> List[Address]:
        raise NotImplementedError()

    def channel(self, token_address: str, partner_address: str):
        raise NotImplementedError()

    def token_network(self, token_address: str):
        raise NotImplementedError()

    def non_settled_partners(self, token_address: str):
        raise NotImplementedError()

    def pending_transfers(self):
        raise NotImplementedError()

    def pending_transfers_by_token(self, token_address: str):
        raise NotImplementedError()

    def pending_transfers_by_token(self, token_address: str, partner_address: str):
        raise NotImplementedError()

    def open_channel(self, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError()

    def close_channel(self, token_address: str, partner_address: str):
        raise NotImplementedError()

    def chanel_increase_deposit(self, token_address: str, partner_address: str):
        raise NotImplementedError()

    def chanel_withdraw_tokens(self, token_address: str, partner_address: str):
        raise NotImplementedError()

    def connections(self):
        raise NotImplementedError()

    def connect_network(self, token_address: str):
        raise NotImplementedError()

    def disconnect_network(self, token_address: str):
        raise NotImplementedError()

    def payment(self, token_address: str, target_address: str):
        raise NotImplementedError()

    def payment_history(self, token_address: str, target_address: str):
        raise NotImplementedError()

    def mint_tokens(self):
        raise NotImplementedError()
