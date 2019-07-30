import argparse

from raidenpy.api import Client


RAIDEN_COMMANDS = (
    "address",
    "tokens"
)


def create_parser(parser: argparse.ArgumentParser):
    parser.add_argument("--endpoint", default="http://127.0.0.1:5001/", help="REST API endpoint")
    parser.add_argument("--version", default="v1", help="API version")

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    subparsers.add_parser("address", help="Query node address")
    subparsers.add_parser("tokens", help="Query list of registered tokens")

    register_token = subparsers.add_parser("register-token", help="Registering a token by token address")
    register_token.add_argument("--token-address", required=True, help="Token address")

    channels = subparsers.add_parser("channels", help="Query list of registered tokens")
    channels.add_argument("--token-address", required=False, help="Token address")
    channels.add_argument("--partner-address", required=False, help="Partner address")


def raiden_cli(args):
    client = Client(args.endpoint, args.version)
    if args.command == "address":
        print(f"Node Address: {client.address()}")
    elif args.command == "tokens":
        tokens = "\n - ".join(client.tokens())
        print(f"Tokens:\n - {tokens}")
    elif args.command == "register-token":
        result = client.register_token(args.token_address)
        print(f"Token network address: {result}")
    elif args.command == "channels":
        if args.token_address and args.partner_address:
            result = client.channel(args.token_address, args.partner_address)
        elif args.token_address:
            result = client.channels_by_token(args.token_address)
        else:
            result = client.channels()
        print(result)



def main():
    parser = argparse.ArgumentParser(description="Raiden python client CLI")
    create_parser(parser)
    args = parser.parse_args()
    raiden_cli(args)
