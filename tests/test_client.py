from raiden.api.client import Client


def test_client_version():
    client = Client(endpoint="http://api-url", version="v2")
    assert client.request.endpoint == "http://api-url/api/v2"
