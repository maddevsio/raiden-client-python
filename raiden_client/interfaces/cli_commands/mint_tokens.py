from argparse import ArgumentParser, Namespace, _SubParsersAction

from raiden_client import Client


def configure_parser(arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
    mint_tokens = subparser.add_parser("mint-token", help="API endpoints for testing")
    mint_tokens.add_argument("-t", "--token-address", required=True, help="Target address")
    mint_tokens.add_argument("--to", required=True, help="The address to assign the minted tokens to")
    mint_tokens.add_argument("--value", required=True, help="he amount of tokens to be minted")
    mint_tokens.add_argument("--contract-method", required=False, help="The name of the contract’s minting method")
    mint_tokens.set_defaults(func=parser_function)


def parser_function(args: Namespace) -> None:
    c = Client()
    c.mint_tokens(
        token_address=args.token_address,
        to=args.to,
        value=args.value,
        contract_method=args.contract_method,
    )
