from eth_utils.address import is_address


def validate_address(address: str) -> bool:
    return is_address(address)
