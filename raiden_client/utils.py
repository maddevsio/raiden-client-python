from web3 import Web3


def normalize_address_eip55(address: str) -> str:
    """Normalize address to EIP55 standard."""
    if not address:
        return address
    return Web3.toChecksumAddress(address)
