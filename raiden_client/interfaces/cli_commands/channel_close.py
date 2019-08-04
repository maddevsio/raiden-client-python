from argparse import ArgumentParser, Namespace, _SubParsersAction

from raiden_client import Client, utils


def configure_parser(arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
    channel_close = subparser.add_parser("channel-close", help="Close a channell")
    channel_close.add_argument("-t", "--token-address", required=True, help="The token we want to be used")
    channel_close.add_argument("-p", "--partner-address", required=True, help="Channel partner address")
    channel_close.set_defaults(func=parser_function)


def parser_function(args: Namespace) -> str:
    client = Client(endpoint=args.endpoint, version=args.version)
    channel = client.channel_close(
        token_address=args.token_address,
        partner_address=args.partner_address,
    )
    return utils.print_stdout(channel)
