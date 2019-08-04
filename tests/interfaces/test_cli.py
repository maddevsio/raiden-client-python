import argparse
import importlib
import sys

from raiden_client.interfaces.cli import CLI_ENDPOINTS, main


def test_cli() -> None:
    """Simple test which just try to build CLI parser"""
    # When we run pytest tests/ , tests/ arg passed to CLI,
    # So we should remove this argument:
    sys.argv.pop()
    assert main() is None


def test_each_command_has_executor() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    for plugin in CLI_ENDPOINTS:
        module = importlib.import_module(plugin)
        module.configure_parser(parser, subparsers)
