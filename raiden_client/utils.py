import importlib
from web3 import Web3


def normalize_address_eip55(address: str) -> str:
    """Normalize address to EIP55 standard."""
    if not address:
        return address
    return Web3.toChecksumAddress(address)


def import_endpoint(path: str):
    """Import package from string."""
    splited_path = path.split(".")
    module = importlib.import_module(".".join(splited_path[:-1]))
    class_name = splited_path[-1]
    return getattr(module, class_name)
