from argparse import ArgumentParser, Namespace, _SubParsersAction

from raiden_client import Client


def configure_parser(arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
    channels = subparser.add_parser("channels", help="Request a list of all unsettled channels")
    channels.add_argument("-t", "--token-address", required=False, help="For the given token address")
    channels.set_defaults(func=parser_function)


def parser_function(args: Namespace) -> None:
    c = Client()
    c.channels(token_address=args.token_address)
