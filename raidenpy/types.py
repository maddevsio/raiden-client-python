from typing import NewType

from mypy_extensions import TypedDict

Address = NewType("Address", str)


class ChannelType(TypedDict):
    token_network_address: Address
    channel_identifier: int
    partner_address: Address
    token_address: Address
    balance: int
    total_deposit: int
    total_withdraw: int
    state: str  # "opened"
    settle_timeout: int
    reveal_timeout: int
