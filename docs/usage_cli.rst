Command Line Interface
======================

Meta queries
------------

Query node address
~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ raiden-cli address


Channel Management
------------------

Get a list of all unsettled channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: shell

    $ raiden-cli channels



List channels for the given token address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ raiden-cli channels --token-address 0x145737846791E749f96344135Ce211BE8C510a17


Query information about one of your channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ raiden-cli channel \
        --token-address 0x145737846791E749f96344135Ce211BE8C510a17 \
        --partner-address 0x145737846791E749f96344135Ce211BE8C510a18


Create channel
~~~~~~~~~~~~~~

.. code-block:: shell

    $ raiden-cli channel-open \
        --token-address 0x145737846791E749f96344135Ce211BE8C510a17 \
        --partner-address 0x145737846791E749f96344135Ce211BE8C510a18 \
        --settle-timeout 100 \
        --total-deposit 3000

Close channel
~~~~~~~~~~~~~

.. code-block:: shell

    $ raiden-cli  channel-close \
        --token-address 0x145737846791E749f96344135Ce211BE8C510a17 \
        --partner-address 0x145737846791E749f96344135Ce211BE8C510a18


Increase channel deposit
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ raiden-cli deposit-increase \
        --token-address 0x145737846791E749f96344135Ce211BE8C510a17 \
        --partner-address 0x145737846791E749f96344135Ce211BE8C510a18 \
        --total-deposit 3400


Withdraw tokens
~~~~~~~~~~~~~~~

.. code-block:: shell

    $ raiden-cli withdraw-increase \
        --token-address 0x145737846791E749f96344135Ce211BE8C510a17 \
        --partner-address 0x145737846791E749f96344135Ce211BE8C510a18 \
        --total-withdraw 3400


Query information about Tokens
------------------------------

List of registered tokens addresses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ raiden-cli tokens


Non-settled channels of partners for a certain token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ raiden-cli non-settled --token-address 0x145737846791E749f96344135Ce211BE8C510a17


Connections Management
----------------------

List all joined token networks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ raiden-cli connections


Join a token network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ raiden-cli connect \
        --token-address 0x145737846791E749f96344135Ce211BE8C510a17 \
        --funds 3400 \
        --initial-channel-target 10 \
        --joinable-funds-target 20


Leave a token network
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ raiden-cli disconnect --token-address 0x145737846791E749f96344135Ce211BE8C510a17

Payments
--------

Make a Payment
~~~~~~~~~~~~~~

.. code-block:: shell

    $ raiden-cli payment \
        --token-address 0x145737846791E749f96344135Ce211BE8C510a17 \
        --target-address 0x145737846791E749f96344135Ce211BE8C510a18 \
        --amount 20 \
        --identifier 1


List payment events
~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ raiden-cli payment-events \
        --token-address 0x145737846791E749f96344135Ce211BE8C510a17 \
        --target-address 0x145737846791E749f96344135Ce211BE8C510a18


API endpoint for testing
------------------------

.. code-block:: shell

    $ raiden-cli mint-token \
        --token-address 0x145737846791E749f96344135Ce211BE8C510a17 \
        --to 0x145737846791E749f96344135Ce211BE8C510a18 \
        --value 100 \
        --contract-method mint