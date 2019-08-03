import argparse
import importlib

import argcomplete


CLI_ENDPOINTS = [
    "raiden_client.interfaces.cli_commands.address",
    "raiden_client.interfaces.cli_commands.channel_close",
    "raiden_client.interfaces.cli_commands.channel_deposit",
    "raiden_client.interfaces.cli_commands.channel_open",
    "raiden_client.interfaces.cli_commands.channel",
    "raiden_client.interfaces.cli_commands.channels",
    "raiden_client.interfaces.cli_commands.channel_withdraw",
    "raiden_client.interfaces.cli_commands.connection_disconnect",
    "raiden_client.interfaces.cli_commands.connections_connect",
    "raiden_client.interfaces.cli_commands.connections",
    "raiden_client.interfaces.cli_commands.mint_tokens",
    "raiden_client.interfaces.cli_commands.non_settled_partners",
    "raiden_client.interfaces.cli_commands.payment_events",
    "raiden_client.interfaces.cli_commands.payment",
    "raiden_client.interfaces.cli_commands.pending_transfers",
    "raiden_client.interfaces.cli_commands.token_registry",
    "raiden_client.interfaces.cli_commands.tokens",
]


def create_subparsers(parser: argparse.ArgumentParser, subparser: argparse._SubParsersAction) -> None:
    for plugin in CLI_ENDPOINTS:
        module = importlib.import_module(plugin)
        module.configure_parser(parser, subparser)


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Raiden python client CLI",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--endpoint", default="http://127.0.0.1:5001/", help="REST API endpoint")
    parser.add_argument("--version", default="v1", help="API version")

    subparsers = parser.add_subparsers()
    create_subparsers(parser, subparsers)
    argcomplete.autocomplete(parser)
    return parser


def main() -> None:
    parser = create_parser()
    args = parser.parse_args()
    if hasattr(args, "func"):
        return args.func(args)
    return parser.print_help()
