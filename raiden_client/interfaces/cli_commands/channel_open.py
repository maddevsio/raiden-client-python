from argparse import ArgumentParser, Namespace, _SubParsersAction

from raiden_client import Client, utils


def configure_parser(arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
    channel_open = subparser.add_parser("channel-open", help="Opens / creates a channel")
    channel_open.add_argument("-t", "--token-address", required=True, help="For the given token address")
    channel_open.add_argument("-p", "--partner-address", required=True, help="Channel partner address")
    channel_open.add_argument("--total-deposit", required=True, help="Amount of tokens to be deposited")
    channel_open.add_argument(
        "--settle-timeout", required=True, help="Amount of blocks that the settle timeout should have"
    )
    channel_open.set_defaults(func=parser_function)


def parser_function(args: Namespace) -> str:
    client = Client(endpoint=args.endpoint, version=args.version)
    channel_open = client.channel_open(
        token_address=args.token_address,
        partner_address=args.partner_address,
        total_deposit=args.total_deposit,
        settle_timeout=args.settle_timeout,
    )
    return utils.print_stdout(channel_open)
