from typing import Tuple, Any

from raiden_client.plugins.v1 import (
    AddressPlugin,
    ChannelPlugin,
)


def plugins_registry() -> Tuple[Any]:
    return (
        AddressPlugin,
        ChannelPlugin,
    )
