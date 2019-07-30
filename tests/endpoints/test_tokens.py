from raidenpy.api import Client

client = Client(endpoint="http://localhost:5001")


def test_address():
    assert isinstance(client.tokens(), list)
