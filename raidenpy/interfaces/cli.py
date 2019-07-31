import argparse

from raidenpy import Client

RAIDEN_COMMANDS = ("address", "tokens")


def create_parser(parser: argparse.ArgumentParser):
    parser.add_argument("--endpoint", default="http://127.0.0.1:5001/", help="REST API endpoint")
    parser.add_argument("--version", default="v1", help="API version")

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    subparsers.add_parser("address", help="Query node address")

    tokens = subparsers.add_parser("tokens", help="Query list of registered tokens")
    tokens.add_argument("--token-address", required=False, help="For the given token address")

    register_token = subparsers.add_parser("register-token", help="Registering a token by token address")
    register_token.add_argument("--token-address", required=True, help="Token address")

    channels = subparsers.add_parser("channels", help="Request a list of all unsettled channels")
    channels.add_argument("--token-address", required=False, help="For the given token address")

    channel = subparsers.add_parser("channel", help="Request a channel detail")
    channel.add_argument("--token-address", required=True, help="For the given token address")
    channel.add_argument("--partner-address", required=True, help="For the given partner address")

    non_settled_partners = subparsers.add_parser(
        "non-settled-partners", help="List of partners with non-settled channels for a certain token."
    )
    non_settled_partners.add_argument("--token-address", required=True, help="For the given token address")


def raiden_cli(args):
    client = Client(args.endpoint, args.version)
    if args.command == "address":
        client.address()
    elif args.command == "tokens":
        client.tokens(args.token_address)
    elif args.command == "register-token":
        client.register_token(args.token_address)
    elif args.command == "channels":
        if args.token_address:
            client.channels(args.token_address)
        else:
            client.channels()
    elif args.command == "channel":
        client.channel(args.token_address, args.partner_address)
    elif args.command == "non-settled-partners":
        client.non_settled_partners(args.token_address)


def main():
    parser = argparse.ArgumentParser(description="Raiden python client CLI")
    create_parser(parser)
    args = parser.parse_args()
    raiden_cli(args)
