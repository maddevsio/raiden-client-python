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


class NonSettledPartners(TypedDict):
    partner_address: Address
    channel: str


class PendingTransfer(TypedDict):
    channel_identifier: str
    initiator: Address
    locked_amount: str
    payment_identifier: str
    role: str
    target: Address
    token_address: Address
    token_network_address: Address
    transferred_amount: str


class ConnectionType(TypedDict):
    funds: int
    sum_deposits: int
    channels: int


class PaymentType(TypedDict):
    initiator_address: Address
    target_address: Address
    token_address: Address
    amount: int
    identifier: int


class PaymentEvent(TypedDict):
    event: str
    amount: int
    initiator: Address
    identifier: int
    log_time: str
