Client API usage
================


Meta queries
------------

Check if node is connected
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from raiden_client import Client

    client = Client()

    client.is_connected


Query node address
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from raiden_client import Client

    client = Client()

    client.address()


Channel Management
------------------

Get a list of all unsettled channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

    from raiden_client import Client

    client = Client()

    client.channels()


List channels for the given token address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from raiden_client import Client

    client = Client()

    client.channels(token_address="0x145737846791E749f96344135Ce211BE8C510a17")


Query information about one of your channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from raiden_client import Client

    client = Client()

    client.channel(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0x145737846791E749f96344135Ce211BE8C510a18",
    )


Create channel
~~~~~~~~~~~~~~

.. code-block:: python

    from raiden_client import Client

    client = Client()

    client.channel_open(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0xCcAbA1b954F29b3daD93A9f846f6356692154500",
        total_deposit=35000000,
        settle_timeout=500,
    )


Close channel
~~~~~~~~~~~~~

.. code-block:: python

    from raiden_client import Client

    client = Client()

    client.channel_close(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0xCcAbA1b954F29b3daD93A9f846f6356692154500",
    )

Increase channel deposit
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from raiden_client import Client

    client = Client()

    client.channel_increase_deposit(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0x145737846791E749f96344135Ce211BE8C510a18",
        total_deposit=3400,
    )


Withdraw tokens
~~~~~~~~~~~~~~~

.. code-block:: python

    from raiden_client import Client

    client = Client()

    client.channel_increase_withdraw(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        partner_address="0x145737846791E749f96344135Ce211BE8C510a18",
        total_withdraw=3400,
    )


Query information about Tokens
------------------------------

List of registered tokens addresses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from raiden_client import Client

    client = Client()

    client.tokens()


Non-settled channels of partners for a certain token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from raiden_client import Client

    client = Client()

    client.non_settled_partners(token_address="0x145737846791E749f96344135Ce211BE8C510a17")


Connections Management
----------------------

List all joined token networks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from raiden_client import Client

    client = Client()

    client.connections()


Join a token network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from raiden_client import Client

    client = Client()

    client.connections_connect(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        funds=100,
        initial_channel_target=10,
        joinable_funds_target=20,
    )


Leave a token network
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from raiden_client import Client

    client = Client()

    client.connection_disconnect(token_address="0x145737846791E749f96344135Ce211BE8C510a17")


Payments
--------

Make a Payment
~~~~~~~~~~~~~~

.. code-block:: python

    from raiden_client import Client

    client = Client()

    client.payment(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        target_address="0x145737846791E749f96344135Ce211BE8C510a18",
        amount=20,
        identifier=1,
    )


List payment events
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from raiden_client import Client

    client = Client()

    client.payment_events(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        target_address="0x145737846791E749f96344135Ce211BE8C510a18",
    )


API endpoint for testing
------------------------

.. code-block:: python

    from raiden_client import Client

    client = Client()

    client.mint_tokens(
        token_address="0x145737846791E749f96344135Ce211BE8C510a17",
        to="0x145737846791E749f96344135Ce211BE8C510a18",
        value=100,
        contract_method="mint",
    )
