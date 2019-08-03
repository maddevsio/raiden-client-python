from argparse import ArgumentParser, Namespace, _SubParsersAction

from raiden_client import Client


def configure_parser(arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
    tokens = subparser.add_parser("tokens", help="Query list of registered tokens")
    tokens.add_argument("-t", "--token-address", required=False, help="For the given token address")
    tokens.set_defaults(func=parser_function)


def parser_function(args: Namespace) -> None:
    c = Client()
    c.tokens(token_address=args.token_address)
