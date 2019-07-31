import argparse

from raidenpy import Client


def create_subparsers(subparsers):
    subparsers.add_parser("address", help="Query node address")

    tokens = subparsers.add_parser("tokens", help="Query list of registered tokens")
    tokens.add_argument("--token-address", required=False, help="For the given token address")

    channels = subparsers.add_parser("channels", help="Request a list of all unsettled channels")
    channels.add_argument("--token-address", required=False, help="For the given token address")

    channel = subparsers.add_parser("channel", help="Request a channel detail")
    channel.add_argument("--token-address", required=True, help="For the given token address")
    channel.add_argument("--partner-address", required=True, help="For the given partner address")

    non_settled_partners = subparsers.add_parser(
        "non-settled-partners", help="List of partners with non-settled channels for a certain token."
    )
    non_settled_partners.add_argument("--token-address", required=True, help="For the given token address")

    pending_transfers = subparsers.add_parser(
        "pending-transfers", help="Returns a list of all transfers that have not been completed yet."
    )
    pending_transfers.add_argument("--token-address", required=True, help="For the given token address")
    pending_transfers.add_argument("--partner-address", required=True, help="For the given partner address")

    channel_open = subparsers.add_parser("channel-open", help="Opens / creates a channel")
    channel_open.add_argument("--token-address", required=True, help="The token we want to be used in the channel")
    channel_open.add_argument("--partner-address", required=True, help="The partner we want to open a channel with")
    channel_open.add_argument(
        "--total-deposit", required=True, help="Total amount of tokens to be deposited to the channel"
    )
    channel_open.add_argument(
        "--settle-timeout", required=True, help="The amount of blocks that the settle timeout should have"
    )

    channel_close = subparsers.add_parser("channel-close", help="Close a channell")
    channel_close.add_argument("--token-address", required=True, help="The token we want to be used in the channel")
    channel_close.add_argument("--partner-address", required=True, help="The partner we want to open a channel with")

    channel_deposit = subparsers.add_parser("channel-deposit-increase", help="Increase channel deposit")
    channel_deposit.add_argument("--token-address", required=True, help="The token we want to be used in the channel")
    channel_deposit.add_argument("--partner-address", required=True, help="The partner we want to open a channel with")
    channel_deposit.add_argument("--total-deposit", required=True, help="The increased total deposit")

    channel_withdraw = subparsers.add_parser("channel-withdraw-increase", help="Increase channel deposit")
    channel_withdraw.add_argument("--token-address", required=True, help="The token we want to be used in the channel")
    channel_withdraw.add_argument("--partner-address", required=True, help="The partner we want to open a channel with")
    channel_withdraw.add_argument("--total-withdraw", required=True, help="The increased total withdraw")

    register_token = subparsers.add_parser("token-register", help="Registering a token by token address")
    register_token.add_argument("--token-address", required=True, help="Token address")


def raiden_cli(args: argparse.Namespace):
    client = Client(args.endpoint, args.version)
    if args.command == "address":
        client.address()
    elif args.command == "tokens":
        client.tokens(args.token_address)
    elif args.command == "register-token":
        client.token_register(args.token_address)
    elif args.command == "channels":
        client.channels(args.token_address)
    elif args.command == "channel":
        client.channel(args.token_address, args.partner_address)
    elif args.command == "non-settled-partners":
        client.non_settled_partners(args.token_address)
    elif args.command == "pending-transfers":
        client.pending_transfers(args.token_address, args.partner_address)
    elif args.command == "channel-open":
        client.channel_open(args.token_address, args.partner_address, args.total_deposit, args.settle_timeout)
    elif args.command == "channel-close":
        client.channel_close(args.token_address, args.partner_address)
    elif args.command == "channel-deposit-increase":
        client.channel_increase_deposit(args.token_address, args.partner_address, args.total_deposit)
    elif args.command == "channel-withdraw-increase":
        client.channel_increase_withdraw(args.token_address, args.partner_address, args.total_withdraw)


def main() -> None:
    parser = argparse.ArgumentParser(description="Raiden python client CLI")
    parser.add_argument("--endpoint", default="http://127.0.0.1:5001/", help="REST API endpoint")
    parser.add_argument("--version", default="v1", help="API version")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    create_subparsers(subparsers)

    args = parser.parse_args()
    raiden_cli(args)
