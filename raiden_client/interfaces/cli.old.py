import argparse
import json

from web3 import Web3

from raiden_client import Client




def tokens_func(client: Client, args: argparse.Namespace) -> None:
    token_address = args.token_address
    if token_address:
        token_address = Web3.toChecksumAddress(token_address)
    tokens = client.tokens(token_address)
    print(json.dumps(tokens, indent=2))


def register_token_func(client: Client, args: argparse.Namespace) -> None:
    token_register = client.token_register(args.token_address)
    print(token_register)


def channels_func(client: Client, args: argparse.Namespace) -> None:
    channels = client.channels(args.token_address)
    print(json.dumps(channels, indent=2))


def channel_func(client: Client, args: argparse.Namespace) -> None:
    channel = client.channel(args.token_address, args.partner_address)
    print(json.dumps(channel, indent=2))


def non_settled_partners_func(client: Client, args: argparse.Namespace) -> None:
    non_settled_partners = client.non_settled_partners(args.token_address)
    print(json.dumps(non_settled_partners, indent=2))


def pending_transfers_func(client: Client, args: argparse.Namespace) -> None:
    pending = client.pending_transfers(args.token_address, args.partner_address)
    print(json.dumps(pending, indent=2))


def channel_open_func(client: Client, args: argparse.Namespace) -> None:
    opened = client.channel_open(
        token_address=args.token_address,
        partner_address=args.partner_address,
        total_deposit=args.total_deposit,
        settle_timeout=args.settle_timeout
    )
    print(json.dumps(opened, indent=2))


def channel_close_func(client: Client, args: argparse.Namespace) -> None:
    output = client.channel_close(args.token_address, args.partner_address)
    print(json.dumps(output, indent=2))


def channel_deposit_increase_func(client: Client, args: argparse.Namespace) -> None:
    output = client.channel_increase_deposit(
        args.token_address,
        args.partner_address,
        args.total_deposit
    )
    print(json.dumps(output, indent=2))


def channel_withdraw_func(client: Client, args: argparse.Namespace) -> None:
    output = client.channel_increase_withdraw(
        args.token_address,
        args.partner_address,
        args.total_withdraw
    )
    print(json.dumps(output, indent=2))


def connections_func(client: Client, args: argparse.Namespace) -> None:
    output = client.connections()
    print(json.dumps(output, indent=2))


def connect_func(client: Client, args: argparse.Namespace) -> None:
    output = client.connections_connect(
        args.token_address,
        args.funds,
        args.initial_channel_target,
        args.joinable_funds_target
    )
    print(json.dumps(output, indent=2))


def connection_disconnect_func(client: Client, args: argparse.Namespace) -> None:
    output = client.connection_disconnect(args.token_address)
    print(json.dumps(output, indent=2))


def payment_func(client: Client, args: argparse.Namespace) -> None:
    output = client.payment(
        token_address=args.token_address,
        target_address=args.target_address,
        amount=args.amount,
        identifier=args.identifier,
    )
    print(json.dumps(output, indent=2))


def payment_events_func(client: Client, args: argparse.Namespace) -> None:
    output = client.payment_events(
        token_address=args.token_address,
        target_address=args.target_address
    )
    print(json.dumps(output, indent=2))


def mint_tokens_func(client: Client, args: argparse.Namespace) -> None:
    output = client.mint_tokens(
        token_address=args.token_address,
        to=args.to,
        value=args.value,
        contract_method=args.contract_method,
    )
    print(json.dumps(output, indent=2))


def create_subparsers(subparsers: argparse._SubParsersAction) -> None:
    pass

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Raiden python client CLI",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--endpoint", default="http://127.0.0.1:5001/", help="REST API endpoint")
    parser.add_argument("--version", default="v1", help="API version")
    subparsers = parser.add_subparsers()
    create_subparsers(subparsers)
    return parser


def main() -> None:
    parser = create_parser()
    args = parser.parse_args()
    client = Client(args.endpoint, args.version)
    if hasattr(args, "func"):
        return args.func(client, args)
    return parser.print_help()
