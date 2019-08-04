Command Line Interface Usage
============================

Query node address
~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    $ raiden-cli address


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

