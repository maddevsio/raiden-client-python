from raidenpy import Client
from raidenpy.types import Address

client = Client(endpoint="http://localhost:5001")


def test_address():
    assert "our_address" in client.address()
    assert len(client.address()["our_address"]) == 42
