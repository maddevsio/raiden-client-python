from argparse import ArgumentParser, Namespace, _SubParsersAction

from raiden_client import Client, utils


def configure_parser(arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
    register_token = subparser.add_parser("token-register", help="Registering a token by token address")
    register_token.add_argument("-t", "--token-address", required=True, help="Token address")
    register_token.set_defaults(func=parser_function)


def parser_function(args: Namespace) -> str:
    client = Client(endpoint=args.endpoint, version=args.version)
    token_network_address = client.token_register(token_address=args.token_address)
    return utils.print_stdout(token_network_address)
