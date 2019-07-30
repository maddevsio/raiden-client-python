import codecs

from eth_utils.address import is_address


def validate_address(address: str) -> bool:
    return is_address(address)


def remove_0x_prefix(value: str) -> str:
    if value.lower().startswith("0x"):
        return value[2:]
    return value


def decode_hex(value: str) -> bytes:
    return codecs.decode(remove_0x_prefix(value), "hex")  # type: ignore
