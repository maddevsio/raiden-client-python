from argparse import ArgumentParser, Namespace, _SubParsersAction

from raiden_client import Client, utils


def configure_parser(arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
    pending_transfers = subparser.add_parser("pending-transfers", help="List of uncompleted transfers")
    pending_transfers.add_argument("-t", "--token-address", required=True, help="For the given token address")
    pending_transfers.add_argument("-p", "--partner-address", required=True, help="For the given partner address")
    pending_transfers.set_defaults(func=parser_function)


def parser_function(args: Namespace) -> str:
    client = Client(endpoint=args.endpoint, version=args.version)
    pending_transfers = client.pending_transfers(
        token_address=args.token_address,
        partner_address=args.partner_address,
    )
    return utils.print_stdout(pending_transfers)
