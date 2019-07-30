# import pytest
# from raidenpy.api import Client

# client = Client("http://localhost")

# ETH_ADDRESS = "0xB8c77482e45F1F44dE1745F52C74426C631bDD52"


# def test_register_token_wrong_address():
#     with pytest.raises(Exception):
#         assert client.register_token("0x")

#     with pytest.raises(Exception):
#         assert client.register_token("0xB8c77482e45F1F44dE1745F52C74426C631bDD521")


# def test_register_token_correct_address():
#     assert client.register_token("0xB8c77482e45F1F44dE1745F52C74426C631bDD52")


# def test_register_token_returns():
#     assert client.register_token(ETH_ADDRESS) == ETH_ADDRESS
