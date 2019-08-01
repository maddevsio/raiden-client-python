# Raiden Network client API
[![Mad Devs](https://mdbadge.glitch.me/mdrw.svg)](https://maddevs.io)
[![CircleCI](https://circleci.com/gh/maddevsio/raiden-client-python.svg?style=svg)](https://circleci.com/gh/maddevsio/raiden-client-python)
[![Maintainability](https://api.codeclimate.com/v1/badges/07b3c04b8ad89893b943/maintainability)](https://codeclimate.com/github/maddevsio/raiden-client-python/maintainability)
[![Codecov](https://img.shields.io/codecov/c/github/maddevsio/raiden-client-python)](https://codecov.io/gh/maddevsio/raiden-client-python)
[![PyPI version](https://badge.fury.io/py/raiden-client.svg)](https://badge.fury.io/py/raiden-client)
[![Documentation Status](https://readthedocs.org/projects/raiden-client-python/badge/?version=latest)](https://raiden-client-python.readthedocs.io/en/latest/?badge=latest)

Client library for Raiden node REST API.


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
```python
>>> from raiden_client import Client

>>> c = Client()
>>> c.address()
>>> c.tokens(token_address="0x2008730f6c4ebde1f4ae0c8b8bf968f53c341c45")

```

### CLI usage

```shell
$ raiden-cli -h
  usage: raiden-cli [-h] [--endpoint ENDPOINT] [--version VERSION]

  Raiden python client CLI

  positional arguments:
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
      connections         Query details of all joined token networks
      connect             Automatically join a token network
      disconnect          Leave a token network
      payment             Initiate a payment
      payment-events      Querying payment events
      mint-token          API endpoints for testing

  optional arguments:
    -h, --help            show this help message and exit
    --endpoint ENDPOINT   REST API endpoint
    --version VERSION     API version

```

<div align="center">
    <h3>Built with Mad Devs support for the community</h3>
    <a href="https://maddevs.io"><img height="100px" src ="docs/md-logo.png" /></a>
</div>
