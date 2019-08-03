# Raiden Node Python Client
[![Mad Devs](https://mdbadge.glitch.me/mdrw.svg)](https://maddevs.io)
[![CircleCI](https://circleci.com/gh/maddevsio/raiden-client-python.svg?style=svg)](https://circleci.com/gh/maddevsio/raiden-client-python)
[![Maintainability](https://api.codeclimate.com/v1/badges/07b3c04b8ad89893b943/maintainability)](https://codeclimate.com/github/maddevsio/raiden-client-python/maintainability)
[![Codecov](https://img.shields.io/codecov/c/github/maddevsio/raiden-client-python)](https://codecov.io/gh/maddevsio/raiden-client-python)
[![PyPI version](https://img.shields.io/pypi/v/raiden-client.svg)](https://pypi.org/project/raiden-client/)
[![Documentation Status](https://readthedocs.org/projects/raiden-client-python/badge/?version=latest)](https://raiden-client-python.readthedocs.io/en/latest/?badge=latest)

Client library for Raiden node REST API. 
Documentation located at [raiden-client-python.readthedocs.io](https://raiden-client-python.readthedocs.io)


## Installation

raiden-client run on Python 3.5+

Install from pypi:

```
$ pip install -U raiden-client
```

Or, clone repo and run:
```
$ pip install .
```

## Usage examples

### API interface
Full docs [here](file:///home/s0b0lev/raiden-python/docs/build/html/client.html)
```python
>>> from raiden_client import Client

>>> c = Client()
>>> c.address()
>>> c.tokens(token_address="0x2008730f6c4ebde1f4ae0c8b8bf968f53c341c45")

```

### CLI usage
Full docs [here](file:///home/s0b0lev/raiden-python/docs/build/html/cli.html)

```shell
$ raiden-cli -h
usage: raiden-cli [-h] [--endpoint ENDPOINT] [--version VERSION]
                  {address,tokens,channels,channel,non-settled,pending-transfers,channel-open,channel-close,deposit-increase,withdraw-increase,token-register,connections,connect,disconnect,payment,payment-events,mint-token}
                  ...

Raiden python client CLI

positional arguments:
  {address,tokens,channels,channel,non-settled,pending-transfers,channel-open,channel-close,deposit-increase,withdraw-increase,token-register,connections,connect,disconnect,payment,payment-events,mint-token}
    address             Query node address
    tokens              Query list of registered tokens
    channels            Request a list of all unsettled channels
    channel             Request a channel detail
    non-settled         Partners with non-settled channels
    pending-transfers   List of uncompleted transfers
    channel-open        Opens / creates a channel
    channel-close       Close a channell
    deposit-increase    Increase channel deposit
    withdraw-increase   Increase channel deposit
    token-register      Registering a token by token address
    connections         Query details of all joined token networks
    connect             Automatically join a token network
    disconnect          Leave a token network
    payment             Initiate a payment
    payment-events      Querying payment events
    mint-token          API endpoints for testing

optional arguments:
  -h, --help            show this help message and exit
  --endpoint ENDPOINT   REST API endpoint (default: http://127.0.0.1:5001/)
  --version VERSION     API version (default: v1)
```

<div align="center">
    <h3>Built with Mad Devs support for the community</h3>
    <a href="https://maddevs.io"><img height="100px" src ="docs/_static/md-logo.png" /></a>
</div>
