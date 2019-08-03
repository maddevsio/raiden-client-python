from argparse import ArgumentParser, Namespace, _SubParsersAction

from raiden_client import Client


def configure_parser(arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
    non_settled_partners = subparser.add_parser("non-settled", help="Partners with non-settled channels")
    non_settled_partners.add_argument("-t", "--token-address", required=True, help="For the given token address")
    non_settled_partners.set_defaults(func=parser_function)


def parser_function(args: Namespace) -> None:
    c = Client()
    c.non_settled_partners(
        token_address=args.token_address,
    )
