import importlib
from unittest import mock

import requests

from raiden_client import Client
from raiden_client.interfaces import cli_commands
from raiden_client.interfaces.cli import CLI_ENDPOINTS, create_main_parser

client = Client()

main_parser = create_main_parser()
subparsers = main_parser.add_subparsers()

# def test_cli() -> None:
#     """Simple test which just try to build CLI parser"""
#     # When we run pytest tests/ , tests/ arg passed to CLI,
#     # So we should remove this argument:
#     sys.argv.pop()
#     assert main() is None


def test_each_command_has_executor() -> None:
    for plugin in CLI_ENDPOINTS:
        module = importlib.import_module(plugin)
        assert hasattr(module, "configure_parser")
        assert hasattr(module, "parser_function")


@mock.patch.object(requests, 'request')
def test_client_disconnected(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 500
    mockresponse.text = "OK"
    mockresponse.return_value = {"our_address": "0x123"}

    assert not client.is_connected


@mock.patch.object(requests, 'request')
def test_client_is_connected(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"
    mockresponse.return_value = {"our_address": "0x123"}

    assert client.is_connected


@mock.patch.object(requests, 'request')
def test_client_address(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"our_address": "0x123"}

    mockresponse.json = json

    output = client.address()
    assert "our_address" in output
    assert output["our_address"] == "0x123"

    cli_commands.address.configure_parser(main_parser, subparsers)

    args = main_parser.parse_args(["address"])
    assert hasattr(args, "func")
    assert args.func(args)


@mock.patch.object(requests, 'request')
def test_client_tokens(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return ["0x123", "0x456"]

    mockresponse.json = json

    output = client.tokens()
    assert "tokens" in output
    assert len(output["tokens"]) > 0

    cli_commands.tokens.configure_parser(main_parser, subparsers)

    args = main_parser.parse_args(["tokens"])

    assert hasattr(args, "func")
    assert args.func(args)


@mock.patch.object(requests, 'request')
def test_client_tokens_filtered(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return ["0x123", "0x456"]

    mockresponse.json = json

    output = client.tokens(token_address="0x145737846791E749f96344135Ce211BE8C510a17")
    assert "tokens" in output
    assert len(output["tokens"]) > 0

    cli_commands.tokens.configure_parser(main_parser, subparsers)

    args = main_parser.parse_args([
        "tokens",
        "--token-address",
        "0x145737846791E749f96344135Ce211BE8C510a17",
    ])

    assert hasattr(args, "func")
    assert args.func(args)


@mock.patch.object(requests, 'request')
def test_client_non_settled_partners(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {
            "non_settled_partners": "0x145737846791E749f96344135Ce211BE8C510a17",
        }

    mockresponse.json = json

    output = client.non_settled_partners(token_address="0x145737846791E749f96344135Ce211BE8C510a17")
    assert "non_settled_partners" in output
    assert len(output["non_settled_partners"]) > 0

    cli_commands.non_settled_partners.configure_parser(main_parser, subparsers)

    args = main_parser.parse_args([
        "non-settled",
        "--token-address",
        "0x145737846791E749f96344135Ce211BE8C510a17",
    ])

    assert hasattr(args, "func")
    assert args.func(args)


@mock.patch.object(requests, 'request')
def test_client_channels(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"channels": []}

    mockresponse.json = json
    channels = client.channels()
    assert "channels" in channels

    cli_commands.channels.configure_parser(main_parser, subparsers)

    args = main_parser.parse_args(["channels"])

    assert hasattr(args, "func")
    assert args.func(args)


@mock.patch.object(requests, 'request')
def test_client_channels_token(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"channels": []}

    mockresponse.json = json
    channels = client.channels(token_address="0x145737846791E749f96344135Ce211BE8C510a17")
    assert "channels" in channels

    cli_commands.channels.configure_parser(main_parser, subparsers)

    args = main_parser.parse_args([
        "channels",
        "--token-address",
        "0x145737846791E749f96344135Ce211BE8C510a17",
    ])

    assert hasattr(args, "func")
    assert args.func(args)


@mock.patch.object(requests, 'request')
def test_client_channel(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"channel": {}}

    mockresponse.json = json
    channel = client.channel(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0x145737846791E749f96344135Ce211BE8C510a18",
    )
    assert "channel" in channel

    cli_commands.channel.configure_parser(main_parser, subparsers)

    args = main_parser.parse_args([
        "channel",
        "--token-address",
        "0x145737846791E749f96344135Ce211BE8C510a17",
        "--partner-address",
        "0x145737846791E749f96344135Ce211BE8C510a18",
    ])

    assert hasattr(args, "func")
    assert args.func(args)


@mock.patch.object(requests, 'request')
def test_client_pending_transfers(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"pending_transfers": {}}

    mockresponse.json = json
    pending_transfers = client.pending_transfers(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0x145737846791E749f96344135Ce211BE8C510a18",
    )
    assert "pending_transfers" in pending_transfers

    cli_commands.pending_transfers.configure_parser(main_parser, subparsers)

    args = main_parser.parse_args([
        "pending-transfers",
        "--token-address",
        "0x145737846791E749f96344135Ce211BE8C510a17",
        "--partner-address",
        "0x145737846791E749f96344135Ce211BE8C510a18",
    ])

    assert hasattr(args, "func")
    assert args.func(args)


@mock.patch.object(requests, 'request')
def test_client_token_register(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"token_network_address": {}}

    mockresponse.json = json
    token_network_address = client.token_register(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
    )
    assert "token_network_address" in token_network_address

    cli_commands.token_registry.configure_parser(main_parser, subparsers)

    args = main_parser.parse_args([
        "token-register",
        "--token-address",
        "0x145737846791E749f96344135Ce211BE8C510a17",
    ])

    assert hasattr(args, "func")
    assert args.func(args)


@mock.patch.object(requests, 'request')
def test_client_channel_open(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"channel": {}}

    mockresponse.json = json
    channel = client.channel_open(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0x145737846791E749f96344135Ce211BE8C510a18",
        settle_timeout=100,
        total_deposit=3000,
    )
    assert "channel" in channel

    cli_commands.channel_open.configure_parser(main_parser, subparsers)

    args = main_parser.parse_args([
        "channel-open",
        "--token-address",
        "0x145737846791E749f96344135Ce211BE8C510a17",
        "--partner-address",
        "0x145737846791E749f96344135Ce211BE8C510a18",
        "--settle-timeout",
        "100",
        "--total-deposit",
        "3000",
    ])

    assert hasattr(args, "func")
    assert args.func(args)


@mock.patch.object(requests, 'request')
def test_client_channel_close(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"channel": {}}

    mockresponse.json = json
    channel = client.channel_close(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0x145737846791E749f96344135Ce211BE8C510a18",
    )
    assert "channel" in channel

    cli_commands.channel_close.configure_parser(main_parser, subparsers)

    args = main_parser.parse_args([
        "channel-close",
        "--token-address",
        "0x145737846791E749f96344135Ce211BE8C510a17",
        "--partner-address",
        "0x145737846791E749f96344135Ce211BE8C510a18",
    ])
    assert hasattr(args, "func")
    assert args.func(args)


@mock.patch.object(requests, 'request')
def test_client_increase_deposit(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"channel": {}}

    mockresponse.json = json
    channel = client.channel_increase_deposit(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0x145737846791E749f96344135Ce211BE8C510a18",
        total_deposit=3400,
    )
    assert "channel" in channel

    cli_commands.channel_deposit.configure_parser(main_parser, subparsers)

    args = main_parser.parse_args([
        "deposit-increase",
        "--token-address",
        "0x145737846791E749f96344135Ce211BE8C510a17",
        "--partner-address",
        "0x145737846791E749f96344135Ce211BE8C510a18",
        "--total-deposit",
        "3400",
    ])
    assert hasattr(args, "func")
    assert args.func(args)


@mock.patch.object(requests, 'request')
def test_client_increase_withdraw(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"channel": {}}

    mockresponse.json = json
    channel = client.channel_increase_withdraw(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0x145737846791E749f96344135Ce211BE8C510a18",
        total_withdraw=3400,
    )
    assert "channel" in channel

    cli_commands.channel_withdraw.configure_parser(main_parser, subparsers)

    args = main_parser.parse_args([
        "withdraw-increase",
        "--token-address",
        "0x145737846791E749f96344135Ce211BE8C510a17",
        "--partner-address",
        "0x145737846791E749f96344135Ce211BE8C510a18",
        "--total-withdraw",
        "3400",
    ])
    assert hasattr(args, "func")
    assert args.func(args)


@mock.patch.object(requests, 'request')
def test_client_connections(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"connections": {}}

    mockresponse.json = json
    connections = client.connections()
    assert "connections" in connections

    cli_commands.connections.configure_parser(main_parser, subparsers)

    args = main_parser.parse_args(["connections"])
    assert hasattr(args, "func")
    assert args.func(args)


@mock.patch.object(requests, 'request')
def test_client_connections_connect(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"connection": {}}

    mockresponse.json = json
    connection = client.connections_connect(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        funds=100,
        initial_channel_target=10,
        joinable_funds_target=20,
    )
    assert "connection" in connection

    cli_commands.connections_connect.configure_parser(main_parser, subparsers)

    args = main_parser.parse_args([
        "connect",
        "--token-address",
        "0x145737846791E749f96344135Ce211BE8C510a17",
        "--funds",
        "3400",
        "--initial-channel-target",
        "10",
        "--joinable-funds-target",
        "20"
    ])
    assert hasattr(args, "func")
    assert args.func(args)


@mock.patch.object(requests, 'request')
def test_client_connections_disconnect(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"connection": {}}

    mockresponse.json = json
    connection = client.connection_disconnect(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
    )
    assert "connection" in connection

    cli_commands.connection_disconnect.configure_parser(main_parser, subparsers)

    args = main_parser.parse_args([
        "disconnect",
        "--token-address",
        "0x145737846791E749f96344135Ce211BE8C510a17",
    ])
    assert hasattr(args, "func")
    assert args.func(args)


@mock.patch.object(requests, 'request')
def test_client_payment(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"payment": {}}

    mockresponse.json = json
    payment = client.payment(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        target_address="0x145737846791E749f96344135Ce211BE8C510a18",
        amount=20,
        identifier=1,
    )
    assert "payment" in payment

    cli_commands.payment.configure_parser(main_parser, subparsers)

    args = main_parser.parse_args([
        "payment",
        "--token-address",
        "0x145737846791E749f96344135Ce211BE8C510a17",
        "--target-address",
        "0x145737846791E749f96344135Ce211BE8C510a18",
        "--amount",
        "20",
        "--identifier",
        "1",
    ])
    assert hasattr(args, "func")
    assert args.func(args)


@mock.patch.object(requests, 'request')
def test_client_payment_events(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"payment_events": {}}

    mockresponse.json = json
    payment_events = client.payment_events(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        target_address="0x145737846791E749f96344135Ce211BE8C510a18",
    )
    assert "payment_events" in payment_events

    cli_commands.payment_events.configure_parser(main_parser, subparsers)

    args = main_parser.parse_args([
        "payment-events",
        "--token-address",
        "0x145737846791E749f96344135Ce211BE8C510a17",
        "--target-address",
        "0x145737846791E749f96344135Ce211BE8C510a18",
    ])
    assert hasattr(args, "func")
    assert args.func(args)


@mock.patch.object(requests, 'request')
def test_client_mint_tokens(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"mint_tokens": {}}

    mockresponse.json = json
    transaction_hash = client.mint_tokens(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        to="0x145737846791E749f96344135Ce211BE8C510a18",
        value=100,
        contract_method="mint",
    )
    assert "transaction_hash" in transaction_hash

    cli_commands.mint_tokens.configure_parser(main_parser, subparsers)

    args = main_parser.parse_args([
        "mint-token",
        "--token-address",
        "0x145737846791E749f96344135Ce211BE8C510a17",
        "--to",
        "0x145737846791E749f96344135Ce211BE8C510a18",
        "--value",
        "100",
        "--contract-method",
        "mint",
    ])
    assert hasattr(args, "func")
    assert args.func(args)
