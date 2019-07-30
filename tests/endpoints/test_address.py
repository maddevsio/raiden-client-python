from raiden.api import Client
from raiden.types import Address

client = Client(endpoint="http://localhost:5001")


def test_address():
    assert isinstance(client.address, bytes)
    assert len(client.address.hex()) == 40
