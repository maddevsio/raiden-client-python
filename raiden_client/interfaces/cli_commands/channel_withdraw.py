from argparse import ArgumentParser, Namespace, _SubParsersAction

from raiden_client import Client, utils


def configure_parser(arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
    channel_withdraw = subparser.add_parser("withdraw-increase", help="Increase channel deposit")
    channel_withdraw.add_argument("-t", "--token-address", required=True, help="For the given token address")
    channel_withdraw.add_argument("-p", "--partner-address", required=True, help="Channel partner address")
    channel_withdraw.add_argument("--total-withdraw", required=True, help="The increased total withdraw")
    channel_withdraw.set_defaults(func=parser_function)


def parser_function(args: Namespace) -> str:
    client = Client(endpoint=args.endpoint, version=args.version)
    channel = client.channel_increase_withdraw(
        token_address=args.token_address,
        partner_address=args.partner_address,
        total_withdraw=args.total_withdraw,
    )
    return utils.print_stdout(channel)
