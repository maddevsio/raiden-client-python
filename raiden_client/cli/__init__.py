from argparse import ArgumentParser, _SubParsersAction

from raiden_client import utils


CLI_ENDPOINTS = [
    "raiden_client.cli.address",
    "raiden_client.cli.channel_close",
    "raiden_client.cli.channel_deposit",
    "raiden_client.cli.channel_open",
    "raiden_client.cli.channel",
    "raiden_client.cli.channels",
    "raiden_client.cli.channel_withdraw",
    "raiden_client.cli.connection_disconnect",
    "raiden_client.cli.connections_connect",
    "raiden_client.cli.connections",
    "raiden_client.cli.mint_tokens",
    "raiden_client.cli.non_settled_partners",
    "raiden_client.cli.payment_events",
    "raiden_client.cli.payment",
    "raiden_client.cli.pending_transfers",
    "raiden_client.cli.token_registry",
    "raiden_client.cli.tokens",
]


def create_subparsers(parser: ArgumentParser, subparser: _SubParsersAction) -> None:
    for plugin in CLI_ENDPOINTS:
        module = utils.import_endpoint(plugin)
        module.configure_parser(parser, subparser)
