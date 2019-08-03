from argparse import ArgumentParser, Namespace, _SubParsersAction

from raiden_client import Client


def configure_parser(arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
    connection_disconnect = subparser.add_parser("disconnect", help="Leave a token network")
    connection_disconnect.add_argument("-t", "--token-address", required=True, help="Token address")
    connection_disconnect.set_defaults(func=parser_function)


def parser_function(args: Namespace) -> None:
    c = Client()
    c.connection_disconnect(token_address=args.token_address)
