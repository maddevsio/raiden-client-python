from typing import List, Any, Dict

from raidenpy import utils
from raidenpy.api.request_handler import Request
from raidenpy.types import Address
from raidenpy.api.base import RaidenAPIv1


class RestAPIv1(RaidenAPIv1):
    version = "v1"

    def __init__(self, endpoint: str) -> None:
        self.request = Request(endpoint, self.version)

    def address(self) -> Address:
        """Get node address.

        Query your address. When raiden starts, you choose an ethereum address 
        which will also be your raiden address.
        """
        raise NotImplementedError()

    def tokens(self) -> List[Address]:
        """Checking if a token is already registered."""
        raise NotImplementedError()

    def register_token(self, token_address: str) -> Address:
        """Registering a token by token address"""
        raise NotImplementedError()

    def channels(self):
        """Get a list of all unsettled channels.

        GET /api/(version)/channels
        """
        raise NotImplementedError()

    def channels_by_token(self, token_address: str):
        """Get a list of all unsettled channels for the given token address.

        GET /api/(version)/channels/(token_address)
        """
        raise NotImplementedError()

    def channel(self, token_address: str, partner_address: str):
        """Query information about one of your channels.

        The channel is specified by the address of the token and the partner’s address.
        GET /api/(version)/channels/(token_address)/(partner_address)
        """
        raise NotImplementedError()

    def token_network(self, token_address: str):
        """Returns the address of the corresponding token network for the given token

        If the token is registered.

        GET /api/(version)/tokens/(token_address)
        """
        raise NotImplementedError()

    def non_settled_partners(self, token_address: str):
        """
        Returns a list of all partners with whom you have non-settled channels for a certain token.
        GET /api/(version)/tokens/(token_address)/partners
        """
        raise NotImplementedError()

    def pending_transfers(self):
        """Returns a list of all transfers that have not been completed yet.

        GET /api/(version)/pending_transfers
        """
        raise NotImplementedError()

    def pending_transfers_by_token(self, token_address: str):
        """ Returns a list of all partners with whom you have non-settled channels for a certain token,
        but limited to pending transfers of the specified token

        GET /api/(version)/pending_transfers/(token_address)
        """
        raise NotImplementedError()

    def pending_transfers_by_token(self, token_address: str, partner_address: str):
        """ Returns a list of all partners with whom you have non-settled channels for a certain token,
        but limited to pending transfers of the specified channel

        GET /api/(version)/pending_transfers/(token_address)/(partner_address)
        """
        raise NotImplementedError()

    def open_channel(
            self,
            partner_address: str,
            settle_timeout: int,
            token_address: str,
            total_deposit: int) -> Dict[str, Any]:
        """Create / Open a channel.

        Args
            token_address   - the address of the token
            partner_address - the address of the partner node
            total_deposit   - the amount of tokens desired for deposit
            settle_timeout  - settlement timeout period
        """
        data = self.request.put("/channels", {
            "partner_address": partner_address,
            "settle_timeout": settle_timeout,
            "token_address": token_address,
            "total_deposit": total_deposit,
        })
        return data

    def close_channel(self, token_address: str, partner_address: str):
        """Close a channel or to increase the deposit in it.

        PATCH /api/(version)/channels/(token_address)/(partner_address)
        {
            "state": "closed"
        }
        """
        raise NotImplementedError()

    def chanel_increase_deposit(self, token_address: str, partner_address: str):
        """Close a channel or to increase the deposit in it.

        PATCH /api/(version)/channels/(token_address)/(partner_address)
        {
            "total_deposit": 100
        }
        """
        raise NotImplementedError()

    def chanel_withdraw_tokens(self, token_address: str, partner_address: str):
        """Close a channel or to increase the deposit in it.

        PATCH /api/(version)/channels/(token_address)/(partner_address)
        {
            "total_withdraw": 100
        }
        """
        raise NotImplementedError()

    def connections(self):
        """Query details of all joined token networks.

        GET /api/(version)/connections
        """
        raise NotImplementedError()

    def connect_network(self, token_address: str):
        """Join a token network.

        PUT /api/(version)/connections/(token_address)
        """
        raise NotImplementedError()

    def disconnect_network(self, token_address: str):
        """Join a token network.

        DELETE /api/(version)/connections/(token_address)
        """
        raise NotImplementedError()

    def payment(self, token_address: str, target_address: str):
        """Initiate a payment.

        POST /api/(version)/payments/(token_address)/(target_address)
        """
        raise NotImplementedError()

    def payment_history(self, token_address: str, target_address: str):
        """Query the payment history.

        GET /api/v1/payments/(token_address)/(target_address)
        """
        raise NotImplementedError()

    def mint_tokens(self):
        """Mint tokens.

        POST /api/(version)/_testing/tokens/(token_address)/mint
        """
        raise NotImplementedError()
