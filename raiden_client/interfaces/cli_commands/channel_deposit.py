from argparse import ArgumentParser, Namespace, _SubParsersAction

from raiden_client import Client, utils


def configure_parser(arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
    channel_deposit = subparser.add_parser("deposit-increase", help="Increase channel deposit")
    channel_deposit.add_argument("-t", "--token-address", required=True, help="For the given token address")
    channel_deposit.add_argument("-p", "--partner-address", required=True, help="Channel partner address")
    channel_deposit.add_argument("--total-deposit", required=True, help="The increased total deposit")
    channel_deposit.set_defaults(func=parser_function)


def parser_function(args: Namespace) -> str:
    client = Client(endpoint=args.endpoint, version=args.version)
    channel = client.channel_increase_deposit(
        token_address=args.token_address,
        partner_address=args.partner_address,
        total_deposit=args.total_deposit,
    )
    return utils.print_stdout(channel)
