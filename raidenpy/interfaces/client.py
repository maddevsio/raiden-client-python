from typing import Any, Dict, List

from raidenpy.api_handler import APIHandler
from raidenpy.endpoints.address import AddressRequest, AddressResponse
from raidenpy.endpoints.channel import ChannelRequest, ChannelResponse
from raidenpy.endpoints.channel_close import (
    ChannelCloseRequest,
    ChannelCloseResponse,
)
from raidenpy.endpoints.channel_deposit import (
    ChannelDepositRequest,
    ChannelDepositResponse,
)
from raidenpy.endpoints.channel_open import (
    ChannelOpenRequest,
    ChannelOpenResponse,
)
from raidenpy.endpoints.channel_withdraw import (
    ChannelWithdrawRequest,
    ChannelWithdrawResponse,
)
from raidenpy.endpoints.channels import ChannelsRequest, ChannelsResponse
from raidenpy.endpoints.token_register import (
    TokenRegistryRequest,
    TokenRegistryResponse,
)
from raidenpy.endpoints.non_settled_partners import (
    NonSettledPartnersRequest,
    NonSettledPartnersResponse,
)
from raidenpy.endpoints.pending_transfers import (
    PendingTransfersRequest,
    PendingTransfersResponse,
)
from raidenpy.endpoints.connections_connect import (
    ConnectionConnectRequest,
    ConnectionConnectResponse,
)
from raidenpy.endpoints.tokens import TokensRequest, TokensResponse
from raidenpy.endpoints.connections import ConnectionsRequest, ConnectionsResponse
from raidenpy.endpoints.connection_disconnect import ConnectionDisconnectRequest, ConnectionDisconnectResponse
from raidenpy.types import (
    Address,
    ChannelType,
    NonSettledPartners,
    PendingTransfer,
)


class Client:
    def __init__(self, endpoint: str, version: str = "v1") -> None:
        self.handler = APIHandler(endpoint, version)

    def address(self) -> Dict[str, Address]:
        request = AddressRequest()
        api_request = self.handler.do(request)
        response = AddressResponse.from_dict(api_request)
        return response.to_dict()

    def tokens(self, token_address: Address = None) -> List[Address]:
        request = TokensRequest(token_address=token_address)
        api_response = self.handler.do(request)
        response = TokensResponse.from_dict({"tokens": api_response})
        return response.to_dict()

    def non_settled_partners(self, token_address: Address) -> Dict[str, List[NonSettledPartners]]:
        request = NonSettledPartnersRequest(token_address=token_address)
        api_response = self.handler.do(request)
        response = NonSettledPartnersResponse.from_dict({"non_settled_partners": api_response})
        return response.to_dict()

    def channels(self, token_address: Address = None) -> List[ChannelType]:
        request = ChannelsRequest()
        response = ChannelsResponse.from_dict({"channels": self.handler.do(request)})
        return response.to_dict()

    def channel(self, token_address: Address, partner_address: Address) -> Dict[str, ChannelType]:
        request = ChannelRequest(token_address=token_address, partner_address=partner_address)
        response = ChannelResponse.from_dict({"channel": self.handler.do(request)})
        return response.to_dict()

    def pending_transfers(
        self, token_address: Address = None, partner_address: Address = None
    ) -> Dict[str, List[PendingTransfer]]:
        request = PendingTransfersRequest(token_address=token_address, partner_address=partner_address)
        api_response = self.handler.do(request)
        response = PendingTransfersResponse.from_dict({"channels": api_response})
        return response.to_dict()

    def token_register(self, token_address: Address) -> Dict[str, Address]:
        request = TokenRegistryRequest(token_address=token_address)
        api_response = self.handler.do(request)
        response = TokenRegistryResponse.from_dict({
            "token_network_address": api_response
        })
        return response.to_dict()

    def channel_open(
        self, token_address: Address, partner_address: Address, settle_timeout: int, total_deposit: int
    ) -> Dict[str, ChannelType]:
        # Update all channel methods to use api_response var
        request = ChannelOpenRequest(
            token_address=token_address,
            partner_address=partner_address,
            settle_timeout=settle_timeout,
            total_deposit=total_deposit,
        )
        response = ChannelOpenResponse.from_dict(self.handler.do(request))
        return response.to_dict()

    def channel_close(self, token_address: Address, partner_address: Address) -> Dict[str, ChannelType]:
        request = ChannelCloseRequest(token_address=token_address, partner_address=partner_address)
        response = ChannelCloseResponse.from_dict(self.handler.do(request))
        return response.to_dict()

    def channel_increase_deposit(
        self, token_address: Address, partner_address: Address, total_deposit: int
    ) -> Dict[str, ChannelType]:
        request = ChannelDepositRequest(
            token_address=token_address, partner_address=partner_address, total_deposit=total_deposit
        )
        response = ChannelDepositResponse.from_dict(self.handler.do(request))
        return response.to_dict()

    def channel_increase_withdraw(self, token_address: Address, partner_address: Address, total_withdraw: int):
        request = ChannelWithdrawRequest(
            token_address=token_address, partner_address=partner_address, total_withdraw=total_withdraw
        )
        response = ChannelWithdrawResponse.from_dict(self.handler.do(request))
        return response.to_dict()

    def connections(self):
        request = ConnectionsRequest()
        api_response = self.handler.do(request)
        response = ConnectionsResponse.from_dict({
            "connections": api_response
        })
        return response.to_dict()

    def connections_connect(self,
                            token_address: Address,
                            funds: int,
                            initial_channel_target: int = None,
                            joinable_funds_target: float = None):
        request = ConnectionConnectRequest(
            token_address=token_address,
            funds=funds,
            initial_channel_target=initial_channel_target,
            joinable_funds_target=joinable_funds_target
        )
        api_response = self.handler.do(request)
        response = ConnectionConnectResponse.from_dict({
            "connection": api_response
        })
        return response.to_dict()

    def connection_disconnect(self, token_address: Address):
        request = ConnectionDisconnectRequest(token_address=token_address)
        api_response = self.handler.do(request)
        response = ConnectionDisconnectResponse.from_dict({
            "connection": api_response
        })
        return response.to_dict()

    def payment(self, token_address: Address, target_address: str):
        """Initiate a payment.
        POST /api/(version)/payments/(token_address)/(target_address)
        """
        pass

    def payment_history(self, token_address: Address, target_address: str):
        """Query the payment history.
        GET /api/v1/payments/(token_address)/(target_address)
        """
        pass

    def mint_tokens(self):
        """Mint tokens.
        POST /api/v1/_testing/tokens/(token_address)/mint
        """
        pass
