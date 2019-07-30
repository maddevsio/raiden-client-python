from raiden.api.client import Client


def test_client_version():
    client = Client(endpoint="http://localhost", version="v2")
    assert client.endpoint == "http://localhost"
    assert client.version == "v2"
