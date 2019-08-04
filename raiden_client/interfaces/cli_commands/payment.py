from argparse import ArgumentParser, Namespace, _SubParsersAction

from raiden_client import Client, utils


def configure_parser(arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
    payment = subparser.add_parser("payment", help="Initiate a payment")
    payment.add_argument("-t", "--token-address", required=True, help="Token address")
    payment.add_argument("--target-address", required=True, help="Target address")
    payment.add_argument("--amount", required=True, help="Token address")
    payment.add_argument("--identifier", required=False, help="Token address")
    payment.set_defaults(func=parser_function)


def parser_function(args: Namespace) -> str:
    client = Client(endpoint=args.endpoint, version=args.version)
    payment = client.payment(
        token_address=args.token_address,
        target_address=args.target_address,
        amount=args.amount,
        identifier=args.identifier,
    )
    return utils.print_stdout(payment)
