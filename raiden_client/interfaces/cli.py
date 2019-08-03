import argparse

import argcomplete

from raiden_client.cli import create_subparsers


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Raiden python client CLI", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--endpoint", default="http://127.0.0.1:5001/", help="REST API endpoint")
    parser.add_argument("--version", default="v1", help="API version")

    subparsers = parser.add_subparsers()
    create_subparsers(parser, subparsers)
    argcomplete.autocomplete(parser)
    return parser


def main() -> None:
    parser = create_parser()
    args = parser.parse_args()
    if hasattr(args, "func"):
        return args.func(args)
    return parser.print_help()
