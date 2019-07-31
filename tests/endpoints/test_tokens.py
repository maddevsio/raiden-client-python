from raidenpy import Client

client = Client(endpoint="http://127.0.0.1:5001")


def test_address():
    assert isinstance(client.tokens(), list)
