import sys
from raiden_client.interfaces.cli import main


def test_cli() -> None:
    """Simple test which just try to build CLI parser"""
    # When we run pytest tests/ , tests/ arg passed to CLI,
    # So we should remove this argument:
    sys.argv.pop()
    assert main() is None
