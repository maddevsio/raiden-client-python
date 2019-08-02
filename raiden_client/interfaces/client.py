from typing import Dict, List

from raiden_client.plugins.v1.address import AddressPlugin
from raiden_client.plugins.v1.channel import ChannelPlugin
from raiden_client.plugins.v1.channel_close import ChannelClose
from raiden_client.plugins.v1.channel_deposit import ChannelDepositPlugin
from raiden_client.plugins.v1.channel_open import ChannelOpenPlugin
from raiden_client.plugins.v1.channel_withdraw import ChannelWithdrawPlugin
from raiden_client.plugins.v1.channels import ChannelsPlugin
from raiden_client.plugins.v1.connection_disconnect import DisconnectPlugin
from raiden_client.plugins.v1.connections import ConnectionsPlugin
from raiden_client.plugins.v1.connections_connect import ConnectPlugin
from raiden_client.plugins.v1.mint_tokens import MintTokensPlugin
from raiden_client.plugins.v1.non_settled_partners import (
    NonSettledPartnersPlugin,
)
from raiden_client.plugins.v1.payment import PaymentPlugin
from raiden_client.plugins.v1.payment_events import PaymentEventsPlugin
from raiden_client.plugins.v1.pending_transfers import PendingTransfersPlugin
from raiden_client.plugins.v1.token_registry import TokenRegisterPlugin
from raiden_client.plugins.v1.tokens import TokensPlugin
from raiden_client.types import (
    ChannelType,
    NonSettledPartners,
    PaymentType,
    PendingTransfer,
)


class Client:
    def __init__(self, endpoint: str, version: str = "v1") -> None:
        self.endpoint = endpoint
        self.version = version

    def address(self) -> Dict[str, str]:
        """Query your address.

        When raiden starts, you choose an ethereum address which will also be your raiden address. 
        """
        plugin = AddressPlugin()
        return plugin.raiden_node_api_interact(self.endpoint)

    def tokens(self, token_address: str = None) -> List[str]:
        """Returns a list of addresses of all registered tokens.

        :params: token_address (address) (optional) Returns the address of token network for the given token
        :returns: list of addresses (or address if toke_address param passed)
        """
        plugin = TokensPlugin(token_address=token_address)
        return plugin.raiden_node_api_interact(self.endpoint)

    def non_settled_partners(self, token_address: str) -> Dict[str, List[NonSettledPartners]]:
        """Returns a list of all partners with whom you have non-settled channels for a certain token.

        :params: token_address (address)
        :returns: list of NonSettledPartners
        """
        plugin = NonSettledPartnersPlugin(token_address=token_address)
        return plugin.raiden_node_api_interact(self.endpoint)

    def channels(self, token_address: str = None) -> List[ChannelType]:
        """Get a list of all unsettled channels.

        :params: token_address (optional) (str) list of all unsettled channels for the given token address.
        :returns: List of channels
        """
        plugin = ChannelsPlugin(token_address=token_address)
        return plugin.raiden_node_api_interact(self.endpoint)

    def channel(self, token_address: str, partner_address: str) -> Dict[str, ChannelType]:
        """Query information about one of your channels.

        The channel is specified by the address of the token and the partner’s address.
        :params: token_address (address)
        :params: partner_address (address)
        :returns: channel dict
        """
        plugin = ChannelPlugin(token_address=token_address, partner_address=partner_address)
        return plugin.raiden_node_api_interact(self.endpoint)

    def pending_transfers(
        self, token_address: str = None, partner_address: str = None
    ) -> Dict[str, List[PendingTransfer]]:
        """Returns a list of all transfers that have not been completed yet.

        :params: token_address (address) (optional) lime results of pending transfers
        :params: partner_address (address) (optional) lime results of pending transfers
        :returns: list of channels
        """
        plugin = PendingTransfersPlugin(token_address=token_address, partner_address=partner_address)
        return plugin.raiden_node_api_interact(self.endpoint)

    def token_register(self, token_address: str) -> Dict[str, str]:
        """Registers a token.
        :params: token_address (str)
        :returns token_network_address (address) – The deployed token networks address.    
        """
        plugin = TokenRegisterPlugin(token_address=token_address)
        return plugin.raiden_node_api_interact(self.endpoint)

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
        plugin = ChannelOpenPlugin(
            token_address=token_address,
            partner_address=partner_address,
            settle_timeout=settle_timeout,
            total_deposit=total_deposit,
        )
        return plugin.raiden_node_api_interact(self.endpoint)

    def channel_close(self, token_address: str, partner_address: str) -> Dict[str, ChannelType]:
        """Close channel.

        :params: token_address (address)
        :params: partner_address (address)
        :returns: channel
        """
        plugin = ChannelClose(token_address=token_address, partner_address=partner_address)
        return plugin.raiden_node_api_interact(self.endpoint)

    def channel_increase_deposit(
        self, token_address: str, partner_address: str, total_deposit: int
    ) -> Dict[str, ChannelType]:
        """Channel increase deposit.

        :params: token_address (address)
        :params: partner_address (address)
        :params: total_deposit (int)
        :returns: channel
        """
        plugin = ChannelDepositPlugin(
            token_address=token_address, partner_address=partner_address, total_deposit=total_deposit
        )
        return plugin.raiden_node_api_interact(self.endpoint)

    def channel_increase_withdraw(self, token_address: str, partner_address: str, total_withdraw: int):
        """Channel increase withdraw.

        :params: token_address (address)
        :params: partner_address (address)
        :params: total_withdraw (int)
        :returns: channel
        """
        plugin = ChannelWithdrawPlugin(
            token_address=token_address, partner_address=partner_address, total_withdraw=total_withdraw
        )
        return plugin.raiden_node_api_interact(self.endpoint)

    def connections(self):
        """Query details of all joined token networks.

        :returns: dict where each key is a token address for which you have open channels
        """
        plugin = ConnectionsPlugin()
        return plugin.raiden_node_api_interact(self.endpoint)

    def connections_connect(
        self, token_address: str, funds: int, initial_channel_target: int = None, joinable_funds_target: float = None
    ):
        """Automatically join a token network.

        The request will only return once all blockchain calls for opening and/or depositing
        to a channel have completed.
        :params: token_address (address)
        :params: funds (int) Amount of funding you want to put into the network
        :params: initial_channel_target (int) (optional) Number of channels to open proactively
        :params: joinable_funds_target (float) (optional) Fraction of funds to join opened channels
        :returns: Connection object
        """
        plugin = ConnectPlugin(
            token_address=token_address,
            funds=funds,
            initial_channel_target=initial_channel_target,
            joinable_funds_target=joinable_funds_target,
        )
        return plugin.raiden_node_api_interact(self.endpoint)

    def connection_disconnect(self, token_address: str):
        """Leave a token network.

        The request will only return once all blockchain calls for closing/settling a channel have completed.
        :params: token_address (address)
        """
        plugin = DisconnectPlugin(token_address=token_address)
        return plugin.raiden_node_api_interact(self.endpoint)

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
        plugin = PaymentPlugin(
            token_address=token_address, target_address=target_address, amount=amount, identifier=identifier
        )
        return plugin.raiden_node_api_interact(self.endpoint)

    def payment_events(self, token_address: str, target_address: str):
        """Query the payment history.

        This includes successful (EventPaymentSentSuccess) and failed (EventPaymentSentFailed) sent
        payments as well as received payments (EventPaymentReceivedSuccess).

        :params: token_address (address) (optional) - filter the list of events
        :params: target_address (address) (optional) - filter the list of events
        :returns: list of payment events
        """
        plugin = PaymentEventsPlugin(token_address=token_address, target_address=target_address)
        return plugin.raiden_node_api_interact(self.endpoint)

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
        plugin = MintTokensPlugin(token_address=token_address, to=to, value=value, contract_method=contract_method)
        return plugin.raiden_node_api_interact(self.endpoint)
