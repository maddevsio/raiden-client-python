Usage
=====

Client
------

Simply use raiden_client.Client interface to interact with Raiden node API.

.. code-blok:: python

    from raiden_client import Client

    c = Client()
    c.address()




CLI
---

It is possible to interact with Raiden Node API via CLI interface.


1. Querying information about your Raiden Node address::

    $ raiden-cli address
    {
        "our_address": "0xe59a5927cbB5007ffF0384244354b158464C47d3"
    }


2. 