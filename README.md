# Raiden Network client API
[![Mad Devs](https://mdbadge.glitch.me/mdrw.svg)](https://maddevs.io)
![Codecov](https://img.shields.io/codecov/c/github/maddevsio/raiden-client-python)
[![CircleCI](https://circleci.com/gh/maddevsio/raiden-client-python.svg?style=svg)](https://circleci.com/gh/maddevsio/raiden-client-python)
[![PyPI version](https://badge.fury.io/py/raiden-client.svg)](https://badge.fury.io/py/raiden-client)
![Read the Docs](https://img.shields.io/readthedocs/raiden-client-python)

A Python client for a Raiden node.

## Installation

```
$ pip install -U raiden-client
```

## Usage

### API interface
```python
>>> from raiden_client import Client

>>> c = Client(endpoint="http://127.0.0.1:5001")
>>> c.address()
>>> c.tokens()
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
