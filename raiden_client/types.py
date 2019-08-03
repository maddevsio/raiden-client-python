from mypy_extensions import TypedDict


class ChannelType(TypedDict):
    token_network_address: str
    channel_identifier: int
    partner_address: str
    token_address: str
    balance: int
    total_deposit: int
    total_withdraw: int
    state: str  # "opened"
    settle_timeout: int
    reveal_timeout: int


class NonSettledPartners(TypedDict):
    partner_address: str
    channel: str


class PendingTransfer(TypedDict):
    channel_identifier: str
    initiator: str
    locked_amount: str
    payment_identifier: str
    role: str
    target: str
    token_address: str
    token_network_address: str
    transferred_amount: str


class ConnectionType(TypedDict):
    funds: int
    sum_deposits: int
    channels: int


class PaymentType(TypedDict):
    initiator_address: str
    target_address: str
    token_address: str
    amount: int
    identifier: int


class PaymentEvent(TypedDict):
    event: str
    amount: int
    initiator: str
    identifier: int
    log_time: str
