from argparse import ArgumentParser, Namespace, _SubParsersAction

from raiden_client import Client, utils


def configure_parser(arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
    channel = subparser.add_parser("channel", help="Request a channel detail")
    channel.add_argument("-t", "--token-address", required=True, help="For the given token address")
    channel.add_argument("-p", "--partner-address", required=True, help="For the given partner address")
    channel.set_defaults(func=parser_function)


def parser_function(args: Namespace) -> str:
    client = Client(endpoint=args.endpoint, version=args.version)
    channel = client.channel(
        token_address=args.token_address,
        partner_address=args.partner_address,
    )
    return utils.print_stdout(channel)
