from raiden.api import Client

client = Client(endpoint="http://localhost:5001")


def test_address():
    assert client.token
