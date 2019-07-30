# Raiden Network client API
[![Mad Devs](https://maddevs.io/badge-dark.svg)](https://maddevs.io)
[![CircleCI](https://circleci.com/gh/s0b0lev/raiden-python.svg?style=svg&circle-token=e688d9f340fa59202c712ef5e2b8affa614b650c)](https://circleci.com/gh/s0b0lev/raiden-python)

A Python client for a Raiden node.

## Features

## CLI interface

```
$ raiden-cli address

$ raiden-cli tokens

$ raiden-cli register-token --token-address <token address>

$ raiden-cli channels
```

### Supported API

#### Querying Information About Your Raiden Node
- [x] Query your address

#### Deploying
- [x] Deploy token
- [x] Get a list of all unsettled channels.
- [ ] Get a list of all unsettled channels for the given token address.

#### Querying Information About Channels and Tokens
- [ ] Query information about one of your channels
- [ ] Returns a list of addresses of all registered tokens.
- [ ] Returns the address of the corresponding token network for the given token, if the token is registered.
- [ ] Returns a list of all partners with whom you have non-settled channels for a certain token.
- [ ] Returns a list of all transfers that have not been completed yet.
- [ ] Like above, but limited to pending transfers of the specified token.
- [ ] Like above, but limited to the specified channel.

#### Channel Management
- [ ] Opens (i. e. creates) a channel.
- [ ] This request is used to close a channel or to increase the deposit in it.

#### Connection Management
- [ ] Query details of all joined token networks
- [ ] Automatically join a token network
- [ ] Leave a token network

#### Payments
- [ ] Initiate a payment.

#### Querying Events
- [ ] Query the payment history
- [ ] Mint tokens
