# Raiden Network client API
[![Mad Devs](https://mdbadge.glitch.me/mdrw.svg)](https://maddevs.io)
[![CircleCI](https://circleci.com/gh/s0b0lev/raiden-python.svg?style=svg&circle-token=e688d9f340fa59202c712ef5e2b8affa614b650c)](https://circleci.com/gh/s0b0lev/raiden-python)

A Python client for a Raiden node.

## Installation

```
$ pip install raidenpy
```

## Usage

Raidenpy client provide few interfaces:
1. CLI
2. API

### CLI usage

```shell
$ raiden-cli -h
usage: raiden-cli [-h] [--endpoint ENDPOINT] [--version VERSION]
                  {address,tokens,channels,channel,non-settled-partners,pending-transfers,channel-open,channel-close,channel-deposit-increase,channel-withdraw-increase,token-register}
                  ...

Raiden python client CLI

positional arguments:
  {address,tokens,channels,channel,non-settled-partners,pending-transfers,channel-open,channel-close,channel-deposit-increase,channel-withdraw-increase,token-register}
                        Commands
    address             Query node address
    tokens              Query list of registered tokens
    channels            Request a list of all unsettled channels
    channel             Request a channel detail
    non-settled-partners
                        List of partners with non-settled channels for a
                        certain token.
    pending-transfers   Returns a list of all transfers that have not been
                        completed yet.
    channel-open        Opens / creates a channel
    channel-close       Close a channell
    channel-deposit-increase
                        Increase channel deposit
    channel-withdraw-increase
                        Increase channel deposit
    token-register      Registering a token by token address

optional arguments:
  -h, --help            show this help message and exit
  --endpoint ENDPOINT   REST API endpoint
  --version VERSION     API version
```

### API interface
```python
>>> from raidenpy import Client

>>> c = Client(endpoint="http://127.0.0.1:5001")
>>> c.address()
>>> c.tokens()
```
