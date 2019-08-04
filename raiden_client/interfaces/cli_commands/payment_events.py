from argparse import ArgumentParser, Namespace, _SubParsersAction

from raiden_client import Client, utils


def configure_parser(arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
    payment_events = subparser.add_parser("payment-events", help="Querying payment events")
    payment_events.add_argument("-t", "--token-address", required=True, help="Target address")
    payment_events.add_argument("--target-address", required=True, help="Token address")
    payment_events.set_defaults(func=parser_function)


def parser_function(args: Namespace) -> str:
    client = Client(endpoint=args.endpoint, version=args.version)
    payment_events = client.payment_events(
        token_address=args.token_address,
        target_address=args.token_address,
    )
    return utils.print_stdout(payment_events)
