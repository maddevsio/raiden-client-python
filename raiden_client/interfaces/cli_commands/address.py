from argparse import ArgumentParser, Namespace, _SubParsersAction

from raiden_client import Client, utils


def configure_parser(arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
    address = subparser.add_parser("address", help="Query node address")
    address.set_defaults(func=parser_function)


def parser_function(args: Namespace) -> str:
    client = Client()
    address = client.address()
    return utils.print_stdout(address)
