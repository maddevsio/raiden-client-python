import argparse

from raidenpy.api import Client

RAIDEN_COMMANDS  = (
    "address",
    "tokens"
)


def create_parser(parser: argparse.ArgumentParser):
    parser.add_argument("--endpoint", default="http://127.0.0.1:5001/", help="REST API endpoint")
    parser.add_argument("--version", default="v1", help="API version")

    subparsers = parser.add_subparsers(dest="command", help="Commands")
    subparsers.add_parser(
        RAIDEN_COMMANDS[0],
        help="Raiden API",
        # parents=[rpc_parser, utilities_parser, input_parser, output_parser],
        aliases=RAIDEN_COMMANDS[1:],
    )


def raiden_cli(args):
    client = Client(args.endpoint, args.version)
    if args.command == "address":
        print(f"Node Address: {client.address()}")
    elif args.command == "tokens":
        tokens = "\n - ".join(client.tokens())
        print(f"Tokens:\n - {tokens}")


def main():
    parser = argparse.ArgumentParser(description="Raiden python client CLI")
    create_parser(parser)
    args = parser.parse_args()
    raiden_cli(args)
