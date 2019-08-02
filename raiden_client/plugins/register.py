from typing import Tuple, Any

from raiden_client.plugins.v1 import (
    AddressPlugin,
)


def plugins_registry() -> Tuple[Any]:
    return (
        AddressPlugin,
    )
