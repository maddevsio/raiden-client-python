import argparse

from raiden_client import Client


def address_func(client: Client, args: argparse.Namespace) -> None:
    address = client.address()
    print(address)


def tokens_func(client: Client, args: argparse.Namespace) -> None:
    client.tokens(args.token_address)


def register_token_func(client: Client, args: argparse.Namespace) -> None:
    client.token_register(args.token_address)


def channels_func(client: Client, args: argparse.Namespace) -> None:
    client.channels(args.token_address)


def channel_func(client: Client, args: argparse.Namespace) -> None:
    client.channel(args.token_address, args.partner_address)


def non_settled_partners_func(client: Client, args: argparse.Namespace) -> None:
    client.non_settled_partners(args.token_address)


def pending_transfers_func(client: Client, args: argparse.Namespace) -> None:
    client.pending_transfers(args.token_address, args.partner_address)


def channel_open_func(client: Client, args: argparse.Namespace) -> None:
    client.channel_open(args.token_address, args.partner_address, args.total_deposit, args.settle_timeout)


def channel_close_func(client: Client, args: argparse.Namespace) -> None:
    client.channel_close(args.token_address, args.partner_address)


def channel_deposit_increase_func(client: Client, args: argparse.Namespace) -> None:
    client.channel_increase_deposit(args.token_address, args.partner_address, args.total_deposit)


def channel_withdraw_func(client: Client, args: argparse.Namespace) -> None:
    client.channel_increase_withdraw(args.token_address, args.partner_address, args.total_withdraw)


def connections_func(client: Client, args: argparse.Namespace) -> None:
    client.connections()


def connect_func(client: Client, args: argparse.Namespace) -> None:
    client.connections_connect(args.token_address, args.funds, args.initial_channel_target, args.joinable_funds_target)


def connection_disconnect_func(client: Client, args: argparse.Namespace) -> None:
    client.connection_disconnect(args.token_address)


def payment_func(client: Client, args: argparse.Namespace) -> None:
    client.payment(
        token_address=args.token_address,
        target_address=args.target_address,
        amount=args.amount,
        identifier=args.identifier,
    )


def payment_events_func(client: Client, args: argparse.Namespace) -> None:
    client.payment_events(token_address=args.token_address, target_address=args.target_address)


def mint_tokens_func(client: Client, args: argparse.Namespace) -> None:
    client.mint_tokens(
        token_address=args.token_address, to=args.to, value=args.value, contract_method=args.contract_method
    )


def create_subparsers(subparsers: argparse._SubParsersAction) -> None:
    address = subparsers.add_parser("address", help="Query node address")
    address.set_defaults(func=address_func)

    tokens = subparsers.add_parser("tokens", help="Query list of registered tokens")
    tokens.add_argument("--token-address", required=False, help="For the given token address")
    tokens.set_defaults(func=tokens_func)

    channels = subparsers.add_parser("channels", help="Request a list of all unsettled channels")
    channels.add_argument("--token-address", required=False, help="For the given token address")
    channels.set_defaults(func=channels_func)

    channel = subparsers.add_parser("channel", help="Request a channel detail")
    channel.add_argument("--token-address", required=True, help="For the given token address")
    channel.add_argument("--partner-address", required=True, help="For the given partner address")
    channel.set_defaults(func=channel_func)

    non_settled_partners = subparsers.add_parser(
        "non-settled-partners", help="List of partners with non-settled channels for a certain token."
    )
    non_settled_partners.add_argument("--token-address", required=True, help="For the given token address")
    non_settled_partners.set_defaults(func=non_settled_partners_func)

    pending_transfers = subparsers.add_parser(
        "pending-transfers", help="Returns a list of all transfers that have not been completed yet."
    )
    pending_transfers.add_argument("--token-address", required=True, help="For the given token address")
    pending_transfers.add_argument("--partner-address", required=True, help="For the given partner address")
    pending_transfers.set_defaults(func=pending_transfers_func)

    channel_open = subparsers.add_parser("channel-open", help="Opens / creates a channel")
    channel_open.add_argument("--token-address", required=True, help="The token we want to be used in the channel")
    channel_open.add_argument("--partner-address", required=True, help="The partner we want to open a channel with")
    channel_open.add_argument(
        "--total-deposit", required=True, help="Total amount of tokens to be deposited to the channel"
    )
    channel_open.add_argument(
        "--settle-timeout", required=True, help="The amount of blocks that the settle timeout should have"
    )
    channel_open.set_defaults(func=channel_open_func)

    channel_close = subparsers.add_parser("channel-close", help="Close a channell")
    channel_close.add_argument("--token-address", required=True, help="The token we want to be used in the channel")
    channel_close.add_argument("--partner-address", required=True, help="The partner we want to open a channel with")
    channel_close.set_defaults(func=channel_close_func)

    channel_deposit = subparsers.add_parser("channel-deposit-increase", help="Increase channel deposit")
    channel_deposit.add_argument("--token-address", required=True, help="The token we want to be used in the channel")
    channel_deposit.add_argument("--partner-address", required=True, help="The partner we want to open a channel with")
    channel_deposit.add_argument("--total-deposit", required=True, help="The increased total deposit")
    channel_deposit.set_defaults(func=channel_deposit_increase_func)

    channel_withdraw = subparsers.add_parser("channel-withdraw-increase", help="Increase channel deposit")
    channel_withdraw.add_argument("--token-address", required=True, help="The token we want to be used in the channel")
    channel_withdraw.add_argument("--partner-address", required=True, help="The partner we want to open a channel with")
    channel_withdraw.add_argument("--total-withdraw", required=True, help="The increased total withdraw")
    channel_withdraw.set_defaults(func=channel_withdraw_func)

    register_token = subparsers.add_parser("token-register", help="Registering a token by token address")
    register_token.add_argument("--token-address", required=True, help="Token address")
    register_token.set_defaults(func=register_token_func)

    connections = subparsers.add_parser("connections", help="Query details of all joined token networks")
    connections.set_defaults(func=connections_func)

    connect = subparsers.add_parser("connect", help="Automatically join a token network")
    connect.add_argument("--token-address", required=True, help="Token address")
    connect.add_argument("--funds", required=True, help="Token address")
    connect.add_argument("--initial-channel-target", required=False, help="Token address")
    # TODO: Update default type to float
    connect.add_argument("--joinable-funds-target", required=False, help="Token address")
    connect.set_defaults(func=connect_func)

    connection_disconnect = subparsers.add_parser("disconnect", help="Leave a token network")
    connection_disconnect.add_argument("--token-address", required=True, help="Token address")
    connection_disconnect.set_defaults(func=connection_disconnect_func)

    payment = subparsers.add_parser("payment", help="Initiate a payment")
    payment.add_argument("--token-address", required=True, help="Token address")
    payment.add_argument("--target-address", required=True, help="Target address")
    payment.add_argument("--amount", required=True, help="Token address")
    payment.add_argument("--identifier", required=False, help="Token address")
    payment.set_defaults(func=payment_func)

    payment_events = subparsers.add_parser("payment-events", help="Querying payment events")
    payment_events.add_argument("--token-address", required=True, help="Target address")
    payment_events.add_argument("--target-address", required=True, help="Token address")
    payment_events.set_defaults(func=payment_events_func)

    mint_tokens = subparsers.add_parser("mint-token", help="API endpoints for testing")
    mint_tokens.add_argument("--token-address", required=True, help="Target address")
    mint_tokens.add_argument("--to", required=True, help="The address to assign the minted tokens to")
    mint_tokens.add_argument("--value", required=True, help="he amount of tokens to be minted")
    mint_tokens.add_argument("--contract-method", required=False, help="The name of the contract’s minting method")
    mint_tokens.set_defaults(func=mint_tokens_func)


def main() -> None:
    parser = argparse.ArgumentParser(description="Raiden python client CLI")
    parser.add_argument("--endpoint", default="http://127.0.0.1:5001/", help="REST API endpoint")
    parser.add_argument("--version", default="v1", help="API version")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    create_subparsers(subparsers)

    args = parser.parse_args()
    client = Client(args.endpoint, args.version)
    if hasattr(args, "func"):
        args.func(client, args)
