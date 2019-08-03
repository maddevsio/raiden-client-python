from typing import List, Dict, Any

from raiden_client.endpoints.address import Address
from raiden_client.endpoints.channel import Channel
from raiden_client.endpoints.channel_close import ChannelClose
from raiden_client.endpoints.channel_deposit import ChannelDeposit
from raiden_client.endpoints.channel_open import ChannelOpen
from raiden_client.endpoints.channel_withdraw import ChannelWithdraw
from raiden_client.endpoints.channels import Channels
from raiden_client.endpoints.connection_disconnect import Disconnect
from raiden_client.endpoints.connections import Connections
from raiden_client.endpoints.connections_connect import Connect
from raiden_client.endpoints.mint_tokens import MintTokens
from raiden_client.endpoints.non_settled_partners import NonSettledPartners
from raiden_client.endpoints.payment import Payment
from raiden_client.endpoints.payment_events import PaymentEvents
from raiden_client.endpoints.pending_transfers import PendingTransfers
from raiden_client.endpoints.token_registry import TokenRegister
from raiden_client.endpoints.tokens import Tokens
from raiden_client.types import (
    ChannelType,
    ConnectionType,
    PaymentType,
    PaymentEvent,
    PendingTransfer,
)

from raiden_client.raiden_api import RaidenAPI


default_endpoint = "http://127.0.0.1:5001/"


class Client:
    def __init__(self, endpoint: str = default_endpoint, version: str = "v1") -> None:
        self.raiden_api = RaidenAPI(endpoint=endpoint, version=version)

    @property
    def is_connected(self) -> bool:
        """Check if raiden node is connected.

        Try to get address, if excpetion occured - node is not connected
        """
        try:
            self.address()
        except Exception:
            return False
        return True

    def address(self) -> Dict[str, str]:
        """Query your address.

        When raiden starts, you choose an ethereum address which will also be your raiden address. 
        """
        endpoint = Address()
        return self.raiden_api.request(endpoint)

    def tokens(self, token_address: str = None) -> Dict[str, List[str]]:
        """Returns a list of addresses of all registered tokens.

        :params: token_address (address) (optional) Returns the address of token network for the given token
        :returns: list of addresses (or address if toke_address param passed)
        """
        endpoint = Tokens(token_address=token_address)
        return self.raiden_api.request(endpoint)

    def non_settled_partners(self, token_address: str) -> Dict[str, List[NonSettledPartners]]:
        """Returns a list of all partners with whom you have non-settled channels for a certain token.

        :params: token_address (address)
        :returns: list of NonSettledPartners
        """
        endpoint = NonSettledPartners(token_address=token_address)
        return self.raiden_api.request(endpoint)

    def channels(self, token_address: str = None) -> Dict[str, List[ChannelType]]:
        """Get a list of all unsettled channels.

        :params: token_address (optional) (str) list of all unsettled channels for the given token address.
        :returns: List of channels
        """
        endpoint = Channels(token_address=token_address)
        return self.raiden_api.request(endpoint)

    def channel(self, token_address: str, partner_address: str) -> Dict[str, ChannelType]:
        """Query information about one of your channels.

        The channel is specified by the address of the token and the partner’s address.
        :params: token_address (address)
        :params: partner_address (address)
        :returns: channel dict
        """
        endpoint = Channel(token_address=token_address, partner_address=partner_address)
        return self.raiden_api.request(endpoint)

    def pending_transfers(
        self, token_address: str = None, partner_address: str = None
    ) -> Dict[str, List[PendingTransfer]]:
        """Returns a list of all transfers that have not been completed yet.

        :params: token_address (address) (optional) lime results of pending transfers
        :params: partner_address (address) (optional) lime results of pending transfers
        :returns: list of channels
        """
        endpoint = PendingTransfers(token_address=token_address, partner_address=partner_address)
        return self.raiden_api.request(endpoint)

    def token_register(self, token_address: str) -> Dict[str, str]:
        """Registers a token.
        :params: token_address (str)
        :returns token_network_address (address) – The deployed token networks address.    
        """
        endpoint = TokenRegister(token_address=token_address)
        return self.raiden_api.request(endpoint)

    def channel_open(
        self, token_address: str, partner_address: str, settle_timeout: int, total_deposit: int
    ) -> Dict[str, ChannelType]:
        """Opens (i. e. creates) a channel.

        :params: partner_address (address) – The partner we want to open a channel with.
        :params: token_address (address) – The token we want to be used in the channel.
        :params: total_deposit (int) – Total amount of tokens to be deposited to the channel
        :params: settle_timeout (int) – The amount of blocks that the settle timeout should have.
        :returns: channel
        """
        endpoint = ChannelOpen(
            token_address=token_address,
            partner_address=partner_address,
            settle_timeout=settle_timeout,
            total_deposit=total_deposit,
        )
        return self.raiden_api.request(endpoint)

    def channel_close(self, token_address: str, partner_address: str) -> Dict[str, ChannelType]:
        """Close channel.

        :params: token_address (address)
        :params: partner_address (address)
        :returns: channel
        """
        endpoint = ChannelClose(token_address=token_address, partner_address=partner_address)
        return self.raiden_api.request(endpoint)

    def channel_increase_deposit(
        self, token_address: str, partner_address: str, total_deposit: int
    ) -> Dict[str, ChannelType]:
        """Channel increase deposit.

        :params: token_address (address)
        :params: partner_address (address)
        :params: total_deposit (int)
        :returns: channel
        """
        endpoint = ChannelDeposit(
            token_address=token_address, partner_address=partner_address, total_deposit=total_deposit
        )
        return self.raiden_api.request(endpoint)

    def channel_increase_withdraw(self, token_address: str, partner_address: str, total_withdraw: int) -> Dict[str, ChannelType]:
        """Channel increase withdraw.

        :params: token_address (address)
        :params: partner_address (address)
        :params: total_withdraw (int)
        :returns: channel
        """
        endpoint = ChannelWithdraw(
            token_address=token_address,
            partner_address=partner_address,
            total_withdraw=total_withdraw,
        )
        return self.raiden_api.request(endpoint)

    def connections(self) -> Dict[str, List[ConnectionType]]:
        """Query details of all joined token networks.

        :returns: dict where each key is a token address for which you have open channels
        """
        endpoint = Connections()
        return self.raiden_api.request(endpoint)

    def connections_connect(self,
                            token_address: str,
                            funds: int,
                            initial_channel_target: int = None,
                            joinable_funds_target: float = None) -> Dict[str, ConnectionType]:
        """Automatically join a token network.

        The request will only return once all blockchain calls for opening and/or depositing
        to a channel have completed.
        :params: token_address (address)
        :params: funds (int) Amount of funding you want to put into the network
        :params: initial_channel_target (int) (optional) Number of channels to open proactively
        :params: joinable_funds_target (float) (optional) Fraction of funds to join opened channels
        :returns: Connection object
        """
        endpoint = Connect(
            token_address=token_address,
            funds=funds,
            initial_channel_target=initial_channel_target,
            joinable_funds_target=joinable_funds_target,
        )
        return self.raiden_api.request(endpoint)

    def connection_disconnect(self, token_address: str) -> Dict[str, Any]:
        """Leave a token network.

        The request will only return once all blockchain calls for closing/settling a channel have completed.
        :params: token_address (address)
        """
        endpoint = Disconnect(token_address=token_address)
        return self.raiden_api.request(endpoint)

    def payment(
        self, token_address: str, target_address: str, amount: int, identifier: int = None
    ) -> Dict[str, PaymentType]:
        """Initiate a payment.

        :params: token_address (address)
        :params: target_address (address)
        :params: amount (int) – Amount to be sent to the target
        :params: identifier (int) – Identifier of the payment (optional)
        :returns: payment dict object
        """
        endpoint = Payment(
            token_address=token_address, target_address=target_address, amount=amount, identifier=identifier
        )
        return self.raiden_api.request(endpoint)

    def payment_events(self, token_address: str, target_address: str) -> Dict[str, List[PaymentEvent]]:
        """Query the payment history.

        This includes successful (EventPaymentSentSuccess) and failed (EventPaymentSentFailed) sent
        payments as well as received payments (EventPaymentReceivedSuccess).

        :params: token_address (address) (optional) - filter the list of events
        :params: target_address (address) (optional) - filter the list of events
        :returns: list of payment events
        """
        endpoint = PaymentEvents(token_address=token_address, target_address=target_address)
        return self.raiden_api.request(endpoint)

    def mint_tokens(self, token_address: str, to: str, value: int, contract_method: str = "mintFor") -> Dict[str, str]:
        """Mint tokens.
        This requires the token at token_address to implement a minting method with one of the common interfaces:
        - mint(address,uint256)
        - mintFor(uint256,address)
        - increaseSupply(uint256,address)
        Depending on the token, it may also be necessary to have minter privilege.

        :params: token_address (address)
        :params: to (address)
        :params: value (int)
        :params: contract_method (str) (optional) default=mintFor choices: mint, mintFor, increaseSupply
        :returns: transaction_hash
        """
        endpoint = MintTokens(token_address=token_address, to=to, value=value, contract_method=contract_method)
        return self.raiden_api.request(endpoint)
