from typing import Any, Dict, List

from raidenpy.endpoints.address import AddressRequest, AddressResponse
from raidenpy.endpoints.channel import ChannelRequest, ChannelResponse
from raidenpy.endpoints.channels import ChannelsRequest, ChannelsResponse
from raidenpy.endpoints.channels_by_token import ChannelByTokenRequest, ChannelByTokenResponse
from raidenpy.endpoints.deploy_tokens import DeployTokenRequst, DeployTokenResponse
from raidenpy.endpoints.token_network import TokenNetworkRequest, TokenNetworkResponse
from raidenpy.endpoints.tokens import TokensRequest, TokensResponse
from raidenpy.endpoints.pending_transfers import PendingTransfersRequest, PendingTransfersResponse
from raidenpy.api_handler import APIHandler
from raidenpy.types import Address


class Client:
    def __init__(self, endpoint: str, version: str = "v1") -> None:
        self.handler = APIHandler(endpoint, version)

    def address(self) -> Dict[str, Address]:
        request = AddressRequest()
        api_request = self.handler.do(request)
        response = AddressResponse.from_dict(api_request)
        return response.to_dict()

    def tokens(self) -> List[Address]:
        request = TokensRequest()
        api_response = self.handler.do(request)
        response = TokensResponse.from_dict({"tokens": api_response})
        return response.to_dict()

    def register_token(self, token_address: Address) -> Dict[str, Address]:
        request = DeployTokenRequst(token_address=token_address)
        response = DeployTokenResponse.from_dict(self.handler.do(request))
        return response.to_dict()

    def token_network(self, token_address: Address) -> Address:
        request = TokenNetworkRequest(token_address=token_address)
        response = TokenNetworkResponse(response=self.handler.do(request))
        return response.to_dict()

    def non_settled_partners(self, token_address: Address):
        """
        Returns a list of all partners with whom you have non-settled channels for a certain token.
        GET /api/(version)/tokens/(token_address)/partners
        """
        pass

    def pending_transfers(self,
                          token_address: Address = None,
                          partner_address: Address = None):
        request = PendingTransfersRequest(token_address=token_address, partner_address=partner_address)
        api_response = self.handler.do(request)
        response = PendingTransfersResponse.from_dict({"channels": api_response})
        return response.to_dict()

    def channels(self):
        request = ChannelsRequest()
        response = ChannelsResponse(response=self.handler.do(request))
        return response.to_dict()

    def channels_by_token(self, token_address: Address):
        request = ChannelByTokenRequest(token_address=token_address)
        response = ChannelByTokenResponse(response=self.handler.do(request))
        return response.to_dict()

    def channel(self, token_address: Address, partner_address: Address):
        request = ChannelRequest(token_address=token_address, partner_address=partner_address)
        response = ChannelResponse(response=self.handler.do(request))
        return response.to_dict()

    def open_channel(self,
                     partner_address: Address,
                     settle_timeout: int,
                     token_address: Address,
                     total_deposit: int) -> Dict[str, Any]:
        return data

    def close_channel(self, token_address: Address, partner_address: Address):
        """Close a channel .
        PATCH /api/(version)/channels/(token_address)/(partner_address)
        {"state": "closed"}
        """
        pass

    def chanel_increase_deposit(self, token_address: Address, partner_address: Address):
        """Increase the deposit in it.
        PATCH /api/(version)/channels/(token_address)/(partner_address)
        {"total_deposit": 100}
        """
        pass

    def chanel_withdraw_tokens(self,
                               token_address: Address,
                               partner_address: Address,
                               total_withdraw: int):
        """Withdraw tokens.
        PATCH /api/(version)/channels/(token_address)/(partner_address)
        {"total_withdraw": 100}
        """
        pass

    def connections(self):
        """Query details of all joined token networks.
        GET /api/(version)/connections
        """
        pass

    def connect_network(self, token_address: Address):
        """Join a token network.
        PUT /api/(version)/connections/(token_address)
        """
        pass

    def disconnect_network(self, token_address: Address):
        """Join a token network.
        DELETE /api/(version)/connections/(token_address)
        """
        pass

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
