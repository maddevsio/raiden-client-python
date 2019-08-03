import importlib
from typing import Tuple

from raiden_client.plugins import BasePlugin


CLIENT_PLUGINS_V1 = [
    "raiden_client.plugins.v1.address.AddressPlugin",
    "raiden_client.plugins.v1.channel_close.ChannelClose",
    "raiden_client.plugins.v1.channel_deposit.ChannelDepositPlugin",
    "raiden_client.plugins.v1.channel_open.ChannelOpenPlugin",
    "raiden_client.plugins.v1.channel.ChannelPlugin",
    "raiden_client.plugins.v1.channels.ChannelsPlugin",
    "raiden_client.plugins.v1.channel_withdraw.ChannelWithdrawPlugin",
    "raiden_client.plugins.v1.connection_disconnect.DisconnectPlugin",
    "raiden_client.plugins.v1.connections_connect.ConnectPlugin",
    "raiden_client.plugins.v1.connections.ConnectionsPlugin",
    "raiden_client.plugins.v1.mint_tokens.MintTokensPlugin",
    "raiden_client.plugins.v1.non_settled_partners.NonSettledPartnersPlugin",
    "raiden_client.plugins.v1.payment_events.PaymentEventsPlugin",
    "raiden_client.plugins.v1.payment.PaymentPlugin",
    "raiden_client.plugins.v1.pending_transfers.PendingTransfersPlugin",
    "raiden_client.plugins.v1.token_registry.TokenRegisterPlugin",
    "raiden_client.plugins.v1.tokens.TokensPlugin",
]


def import_package(path: str) -> BasePlugin:
    """Import package from string."""
    splited_path = path.split(".")
    module = importlib.import_module(".".join(splited_path[:-1]))
    class_name = splited_path[-1]
    return getattr(module, class_name)


def plugins_registry_v1() -> Tuple[BasePlugin]:
    return tuple(import_package(plugin) for plugin in CLIENT_PLUGINS_V1)
