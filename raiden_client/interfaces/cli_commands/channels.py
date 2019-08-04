from argparse import ArgumentParser, Namespace, _SubParsersAction

from raiden_client import Client, utils


def configure_parser(arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
    channels = subparser.add_parser("channels", help="Request a list of all unsettled channels")
    channels.add_argument("-t", "--token-address", required=False, help="For the given token address")
    channels.set_defaults(func=parser_function)


def parser_function(args: Namespace) -> str:
    client = Client(endpoint=args.endpoint, version=args.version)
    channels = client.channels(token_address=args.token_address)
    return utils.print_stdout(channels)
