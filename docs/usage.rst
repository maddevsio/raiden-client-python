Usage
=====

Client
------

Simply use raiden_client.Client interface to interact with Raiden node API.

.. code-block:: python

    from raiden_client import Client

    c = Client()

    c.address()

    c.payment(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        target_address="0xCcAbA1b954F29b3daD93A9f846f6356692154500",
        amount=10,
    )

    c.channels()


Full list of commands and arguments can be found here:
:doc:`Raiden client API <client>`

CLI
---

It is possible to interact with Raiden Node API via CLI interface.


Querying information about your Raiden Node address::

    $ raiden-cli address

    > "0xe59a5927cbB5007ffF0384244354b158464C47d3"


Returns a list of addresses of all registered tokens.::

    $ raiden-cli tokens

    [
        "0x145737846791E749f96344135Ce211BE8C510a17",
        "0x3b47ae7d1B6B73341c7C9238669500DC3EE322c8",
    ]

or returns the address of the corresponding token network for the given token,
if the token is registered.::

    $ raiden-cli tokens -t 0x145737846791E749f96344135Ce211BE8C510a17

    > "0x40D5A05FD91E91D5fCE9A204C53f5B0347Db0d14"


Full list of commands and arguments can be found here:
:doc:`Command Line Interface (CLI) <cli>`
