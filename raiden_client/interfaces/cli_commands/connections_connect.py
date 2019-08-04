from argparse import ArgumentParser, Namespace, _SubParsersAction

from raiden_client import Client, utils


def configure_parser(arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
    connect = subparser.add_parser("connect", help="Automatically join a token network")
    connect.add_argument("-t", "--token-address", required=True, help="Token address")
    connect.add_argument("--funds", required=True, help="Token address")
    connect.add_argument("--initial-channel-target", required=False, help="Token address")
    connect.add_argument("--joinable-funds-target", type=float, required=False, help="Token address")
    connect.set_defaults(func=parser_function)


def parser_function(args: Namespace) -> str:
    client = Client(endpoint=args.endpoint, version=args.version)
    connection = client.connections_connect(
        token_address=args.token_address,
        funds=args.funds,
        initial_channel_target=args.initial_channel_target,
        joinable_funds_target=args.joinable_funds_target,
    )
    return utils.print_stdout(connection)
