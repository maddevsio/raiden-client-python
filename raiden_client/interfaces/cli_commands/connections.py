from argparse import ArgumentParser, Namespace, _SubParsersAction

from raiden_client import Client, utils


def configure_parser(arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
    connections = subparser.add_parser("connections", help="Query details of all joined token networks")
    connections.set_defaults(func=parser_function)


def parser_function(args: Namespace) -> None:
    client = Client(endpoint=args.endpoint, version=args.version)
    connection = client.connections()
    return utils.print_stdout(connection)
