from typing import Any, Dict, List

from raidenpy.api.request.address import AddressRequest, AddressResponse
from raidenpy.api.request.channel import ChannelRequest, ChannelResponse
from raidenpy.api.request.channels import ChannelsRequest, ChannelsResponse
from raidenpy.api.request.channels_by_token import ChannelByTokenRequest, ChannelByTokenResponse
from raidenpy.api.request.deploy_tokens import DeployTokenRequst, DeployTokenResponse
from raidenpy.api.request.token_network import TokenNetworkRequest, TokenNetworkResponse
from raidenpy.api.request.tokens import TokensRequest, TokensResponse
from raidenpy.api.request_handler import Request
from raidenpy.types import Address


class Client:
    def __init__(self, endpoint: str, version: str = "v1") -> None:
        self.request = Request(endpoint, version)

    def address(self) -> Dict[str, Address]:
        req = AddressRequest()
        response = AddressResponse(response=self.request.do(req))
        return response.to_dict()

    def tokens(self) -> List[Address]:
        req = TokensRequest()
        response = TokensResponse(response=self.request.do(req))
        return response.to_dict()

    def register_token(self, token_address: Address) -> Dict[str, Address]:
        req = DeployTokenRequst(token_address=token_address)
        response = DeployTokenResponse(response=self.request.do(req))
        return response.to_dict()

    def channels(self):
        req = ChannelsRequest()
        response = ChannelsResponse(response=self.request.do(req))
        return response.to_dict()

    def channels_by_token(self, token_address: Address):
        req = ChannelByTokenRequest(token_address=token_address)
        response = ChannelByTokenResponse(response=self.request.do(req))
        return response.to_dict()

    def channel(self, token_address: Address, partner_address: Address):
        req = ChannelRequest(token_address=token_address, partner_address=partner_address)
        response = ChannelResponse(response=self.request.do(req))
        return response.to_dict()

    def token_network(self, token_address: Address) -> Address:
        req = TokenNetworkRequest(token_address=token_address)
        response = TokenNetworkResponse(response=self.request.do(req))
        return response.to_dict()

    def non_settled_partners(self, token_address: str):
        """
        Returns a list of all partners with whom you have non-settled channels for a certain token.
        GET /api/(version)/tokens/(token_address)/partners
        """
        pass

    def pending_transfers(self):
        """Returns a list of all transfers that have not been completed yet.

        GET /api/(version)/pending_transfers
        """
        pass

    def pending_transfers_by_token(self, token_address: str):
        """ Returns a list of all partners with whom you have non-settled channels for a certain token,
        but limited to pending transfers of the specified token

        GET /api/(version)/pending_transfers/(token_address)
        """
        pass

    def pending_transfers_by_token(self, token_address: str, partner_address: str):
        """ Returns a list of all partners with whom you have non-settled channels for a certain token,
        but limited to pending transfers of the specified channel

        GET /api/(version)/pending_transfers/(token_address)/(partner_address)
        """
        pass

    def open_channel(
        self, partner_address: str, settle_timeout: int, token_address: str, total_deposit: int
    ) -> Dict[str, Any]:
        """Create / Open a channel.

        Args
            token_address   - the address of the token
            partner_address - the address of the partner node
            total_deposit   - the amount of tokens desired for deposit
            settle_timeout  - settlement timeout period
        """
        data = self.request.put(
            "/channels",
            {
                "partner_address": partner_address,
                "settle_timeout": settle_timeout,
                "token_address": token_address,
                "total_deposit": total_deposit,
            },
        )
        return data

    def close_channel(self, token_address: str, partner_address: str):
        """Close a channel or to increase the deposit in it.

        PATCH /api/(version)/channels/(token_address)/(partner_address)
        {
            "state": "closed"
        }
        """
        pass

    def chanel_increase_deposit(self, token_address: str, partner_address: str):
        """Close a channel or to increase the deposit in it.

        PATCH /api/(version)/channels/(token_address)/(partner_address)
        {
            "total_deposit": 100
        }
        """
        pass

    def chanel_withdraw_tokens(self, token_address: str, partner_address: str):
        """Close a channel or to increase the deposit in it.

        PATCH /api/(version)/channels/(token_address)/(partner_address)
        {
            "total_withdraw": 100
        }
        """
        pass

    def connections(self):
        """Query details of all joined token networks.

        GET /api/(version)/connections
        """
        pass

    def connect_network(self, token_address: str):
        """Join a token network.

        PUT /api/(version)/connections/(token_address)
        """
        pass

    def disconnect_network(self, token_address: str):
        """Join a token network.

        DELETE /api/(version)/connections/(token_address)
        """
        pass

    def payment(self, token_address: str, target_address: str):
        """Initiate a payment.

        POST /api/(version)/payments/(token_address)/(target_address)
        """
        pass

    def payment_history(self, token_address: str, target_address: str):
        """Query the payment history. 

        GET /api/v1/payments/(token_address)/(target_address)
        """
        pass

    def mint_tokens(self):
        """Mint tokens.

        POST /api/(version)/_testing/tokens/(token_address)/mint
        """
        pass
