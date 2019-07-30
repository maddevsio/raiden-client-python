import pytest
from raiden.api import Client

client = Client("http://localhost")

ETH_ADDRESS = "0xB8c77482e45F1F44dE1745F52C74426C631bDD52"


def test_deploy_wrong_address():
    with pytest.raises(Exception):
        assert client.deploy("0x")

    with pytest.raises(Exception):
        assert client.deploy("0xB8c77482e45F1F44dE1745F52C74426C631bDD521")


def test_deploy_correct_address():
    assert client.deploy("0xB8c77482e45F1F44dE1745F52C74426C631bDD52")


def test_deploy_returns():
    assert client.deploy(ETH_ADDRESS) == ETH_ADDRESS
