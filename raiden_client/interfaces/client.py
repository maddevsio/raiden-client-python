from typing import Any, Dict, List

from raiden_client.api_handler import APIHandler
from raiden_client.endpoints.address import AddressRequest, AddressResponse
from raiden_client.endpoints.channel import ChannelRequest, ChannelResponse
from raiden_client.endpoints.channel_close import (
    ChannelCloseRequest,
    ChannelCloseResponse,
)
from raiden_client.endpoints.channel_deposit import (
    ChannelDepositRequest,
    ChannelDepositResponse,
)
from raiden_client.endpoints.channel_open import (
    ChannelOpenRequest,
    ChannelOpenResponse,
)
from raiden_client.endpoints.channel_withdraw import (
    ChannelWithdrawRequest,
    ChannelWithdrawResponse,
)
from raiden_client.endpoints.channels import ChannelsRequest, ChannelsResponse
from raiden_client.endpoints.connection_disconnect import (
    ConnectionDisconnectRequest,
    ConnectionDisconnectResponse,
)
from raiden_client.endpoints.connections import (
    ConnectionsRequest,
    ConnectionsResponse,
)
from raiden_client.endpoints.connections_connect import (
    ConnectionConnectRequest,
    ConnectionConnectResponse,
)
from raiden_client.endpoints.mint_tokens import (
    MintTokensRequest,
    MintTokensResponse,
)
from raiden_client.endpoints.non_settled_partners import (
    NonSettledPartnersRequest,
    NonSettledPartnersResponse,
)
from raiden_client.endpoints.payment import PaymentRequest, PaymentResponse
from raiden_client.endpoints.payment_events import (
    PaymentEventsRequest,
    PaymentEventsResponse,
)
from raiden_client.endpoints.pending_transfers import (
    PendingTransfersRequest,
    PendingTransfersResponse,
)
from raiden_client.endpoints.token_register import (
    TokenRegistryRequest,
    TokenRegistryResponse,
)
from raiden_client.endpoints.tokens import TokensRequest, TokensResponse
from raiden_client.types import (
    Address,
    ChannelType,
    NonSettledPartners,
    PaymentType,
    PendingTransfer,
)


class Client:
    def __init__(self, endpoint: str, version: str = "v1") -> None:
        self.handler = APIHandler(endpoint, version)

    def address(self) -> Dict[str, Address]:
        """Query your address.

        When raiden starts, you choose an ethereum address which will also be your raiden address. 
        """
        request = AddressRequest()
        api_request = self.handler.do(request)
        response = AddressResponse.from_dict(api_request)
        return response.to_dict()

    def tokens(self, token_address: Address = None) -> List[Address]:
        """Returns a list of addresses of all registered tokens.

        :params: token_address (address) (optional) Returns the address of token network for the given token
        :returns: list of addresses (or address if toke_address param passed)
        """
        request = TokensRequest(token_address=token_address)
        api_response = self.handler.do(request)
        response = TokensResponse.from_dict(api_response)
        return response.to_dict()

    def non_settled_partners(self, token_address: Address) -> Dict[str, List[NonSettledPartners]]:
        """Returns a list of all partners with whom you have non-settled channels for a certain token.

        :params: token_address (address)
        :returns: list of NonSettledPartners
        """
        request = NonSettledPartnersRequest(token_address=token_address)
        api_response = self.handler.do(request)
        response = NonSettledPartnersResponse.from_dict(api_response)
        return response.to_dict()

    def channels(self, token_address: Address = None) -> List[ChannelType]:
        """Get a list of all unsettled channels.

        :params: token_address (optional) (str) list of all unsettled channels for the given token address.
        :returns: List of channels
        """
        request = ChannelsRequest()
        api_response = self.handler.do(request)
        response = ChannelsResponse.from_dict(api_response)
        return response.to_dict()

    def channel(self, token_address: Address, partner_address: Address) -> Dict[str, ChannelType]:
        """Query information about one of your channels.
    
        The channel is specified by the address of the token and the partner’s address.
        :params: token_address (address)
        :params: partner_address (address)
        :returns: channel dict
        """
        request = ChannelRequest(token_address=token_address, partner_address=partner_address)
        api_response = self.handler.do(request)
        response = ChannelResponse.from_dict(api_response)
        return response.to_dict()

    def pending_transfers(self,
                          token_address: Address = None,
                          partner_address: Address = None) -> Dict[str, List[PendingTransfer]]:
        """Returns a list of all transfers that have not been completed yet.

        :params: token_address (address) (optional) lime results of pending transfers
        :params: partner_address (address) (optional) lime results of pending transfers
        :returns: list of channels
        """
        request = PendingTransfersRequest(token_address=token_address, partner_address=partner_address)
        api_response = self.handler.do(request)
        response = PendingTransfersResponse.from_dict(api_response)
        return response.to_dict()

    def token_register(self, token_address: Address) -> Dict[str, Address]:
        """Registers a token.
        :params: token_address (str)
        :returns token_network_address (address) – The deployed token networks address.    
        """
        request = TokenRegistryRequest(token_address=token_address)
        api_response = self.handler.do(request)
        response = TokenRegistryResponse.from_dict(api_response)
        return response.to_dict()

    def channel_open(self,
                     token_address: Address,
                     partner_address: Address,
                     settle_timeout: int,
                     total_deposit: int) -> Dict[str, ChannelType]:
        """Opens (i. e. creates) a channel.
        
        :params: partner_address (address) – The partner we want to open a channel with.
        :params: token_address (address) – The token we want to be used in the channel.
        :params: total_deposit (int) – Total amount of tokens to be deposited to the channel
        :params: settle_timeout (int) – The amount of blocks that the settle timeout should have.
        :returns: channel
        """
        request = ChannelOpenRequest(
            token_address=token_address,
            partner_address=partner_address,
            settle_timeout=settle_timeout,
            total_deposit=total_deposit,
        )
        api_response = self.handler.do(request)
        response = ChannelOpenResponse.from_dict(api_response)
        return response.to_dict()

    def channel_close(self, token_address: Address, partner_address: Address) -> Dict[str, ChannelType]:
        """Close channel.

        :params: token_address (address)
        :params: partner_address (address)
        :returns: channel
        """
        request = ChannelCloseRequest(token_address=token_address, partner_address=partner_address)
        api_response = self.handler.do(request)
        response = ChannelCloseResponse.from_dict(api_response)
        return response.to_dict()

    def channel_increase_deposit(self,
                                 token_address: Address,
                                 partner_address: Address,
                                 total_deposit: int) -> Dict[str, ChannelType]:
        """Channel increase deposit.

        :params: token_address (address)
        :params: partner_address (address)
        :params: total_deposit (int)
        :returns: channel
        """
        request = ChannelDepositRequest(
            token_address=token_address,
            partner_address=partner_address,
            total_deposit=total_deposit
        )
        api_response = self.handler.do(request)
        response = ChannelDepositResponse.from_dict(api_response)
        return response.to_dict()

    def channel_increase_withdraw(self, token_address: Address, partner_address: Address, total_withdraw: int):
        """Channel increase withdraw.

        :params: token_address (address)
        :params: partner_address (address)
        :params: total_withdraw (int)
        :returns: channel
        """
        request = ChannelWithdrawRequest(
            token_address=token_address,
            partner_address=partner_address,
            total_withdraw=total_withdraw
        )
        api_response = self.handler.do(request)
        response = ChannelWithdrawResponse.from_dict(api_response)
        return response.to_dict()

    def connections(self):
        """Query details of all joined token networks.

        :returns: dict where each key is a token address for which you have open channels
        """
        request = ConnectionsRequest()
        api_response = self.handler.do(request)
        response = ConnectionsResponse.from_dict(api_response)
        return response.to_dict()

    def connections_connect(self,
                            token_address: Address,
                            funds: int,
                            initial_channel_target: int = None,
                            joinable_funds_target: float = None):
        """Automatically join a token network.

        The request will only return once all blockchain calls for opening and/or depositing
        to a channel have completed.
        :params: token_address (address)
        :params: funds (int) Amount of funding you want to put into the network
        :params: initial_channel_target (int) (optional) Number of channels to open proactively
        :params: joinable_funds_target (float) (optional) Fraction of funds to join opened channels
        :returns: Connection object
        """
        request = ConnectionConnectRequest(
            token_address=token_address,
            funds=funds,
            initial_channel_target=initial_channel_target,
            joinable_funds_target=joinable_funds_target,
        )
        api_response = self.handler.do(request)
        response = ConnectionConnectResponse.from_dict(api_response)
        return response.to_dict()

    def connection_disconnect(self, token_address: Address):
        """Leave a token network.

        The request will only return once all blockchain calls for closing/settling a channel have completed.
        :params: token_address (address)
        """
        request = ConnectionDisconnectRequest(token_address=token_address)
        api_response = self.handler.do(request)
        response = ConnectionDisconnectResponse.from_dict(api_response)
        return response.to_dict()

    def payment(self,
                token_address: Address,
                target_address: str,
                amount: int,
                identifier: int = None) -> Dict[str, PaymentType]:
        """Initiate a payment.

        :params: token_address (address)
        :params: target_address (address)
        :params: amount (int) – Amount to be sent to the target
        :params: identifier (int) – Identifier of the payment (optional)
        :returns: payment dict object
        """
        request = PaymentRequest(
            token_address=token_address,
            target_address=target_address,
            amount=amount,
            identifier=identifier,
        )
        api_response = self.handler.do(request)
        response = PaymentResponse.from_dict(api_response)
        return response.to_dict()

    def payment_events(self, token_address: Address, target_address: str):
        """Query the payment history.
        
        This includes successful (EventPaymentSentSuccess) and failed (EventPaymentSentFailed) sent 
        payments as well as received payments (EventPaymentReceivedSuccess). 
        
        :params: token_address (address) (optional) - filter the list of events
        :params: target_address (address) (optional) - filter the list of events
        :returns: list of payment events
        """
        request = PaymentEventsRequest(token_address=token_address, target_address=target_address)
        api_response = self.handler.do(request)
        response = PaymentEventsResponse.from_dict(api_response)
        return response.to_dict()

    def mint_tokens(self,
                    token_address: Address,
                    to: str,
                    value: int,
                    contract_method: str = "mintFor") -> Dict[str, str]:
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
        request = MintTokensRequest(
            token_address=token_address,
            to=to,
            value=value,
            contract_method=contract_method
        )
        api_response = self.handler.do(request)
        response = MintTokensResponse.from_dict(api_response)
        return response.to_dict()
