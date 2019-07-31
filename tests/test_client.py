from raidenpy import Client


def test_client_version():
    client = Client(endpoint="http://api-url", version="v2")
    assert client.handler.endpoint == "http://api-url"
