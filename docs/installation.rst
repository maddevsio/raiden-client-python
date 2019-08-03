Installation
============

Install from pypi::

    pip3 install -U raiden-client


or, clone repo and install locally::

    pip3 install .


Enabling tab completion
-----------------------

Raiden client can be configured to auto complete commands when the <tab> key
is pressed.

After installing raiden-client, to activate tab-completion in future bash
prompts, use::

    register-python-argcomplete raiden-client >> ~/.bashrc


For one-time activation of argcomplete for raiden-client, use::

    eval "$(register-python-argcomplete raiden-client)"

