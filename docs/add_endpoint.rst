Implement Raiden API endpoint
=============================

In case if Raiden API add new endpoint client should implement following steps:


Create new endpoint interface
--------------------------------

1. Create new plugin file at **raiden_client/endpoints/**
(like new_endpoint.py)

2. Implement endpoint from BaseEndpoint abstract class

.. code-block:: python

    # raiden_client/endpoints/new_endpoint.py

    from raiden_client.endpoints import BaseEndpoint

    class NewEndpoint(BaseEndpoint):
        # Response data stored in Class attribute
        stored_response = None

        # In case if endpoint require payload, it can be pass via __init__
        def __init__(self, token_address: str) -> None:
            self.token_address = token_address

        @property
        def name(self) -> str:
            # Endpoint unique name (for convention)
            return "new-endpoint"

        @property
        @abstractmethod
        def endpoint(self) -> str:
            # New endpoint URI
            return "/endpoint"

        @property
        def method(self) -> str:
            # HTTP method to interact with endpoint
            return "post"

        def payload(self) -> Dict[str, Any]:
            # Payload to send on Raiden API endpoint
            return {"token_address": self.token_address}

        def from_dict(self, response: Dict[str, Any]) -> None:
            # Load response results into class attribute
            self.stored_response = response

        def to_dict(self) -> Dict[str, Any]:
            # Get endpoint data
            return {"stored_response": self.stored_response}




3. Add new method at Client interface: **raiden_client/interfaces/client.py**

.. code-block:: python

    def new_endpoint(self, token_address: str) -> Dict[str, str]:
        """Query your address."""
        endpoint = NewEndpoint(token_address=token_address)
        # Send request to API via RaidenAPI instance
        return self.raiden_api.request(endpoint)

4. Create new command at raiden_client/interfaces/cli_commands/
(like new_endpoint.py)

.. code-block:: python

    # raiden_client/interfaces/cli_commands/new_endpoint.py content

    from argparse import ArgumentParser, Namespace, _SubParsersAction

    from raiden_client import Client, utils


    def configure_parser(arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
        tokens = subparser.add_parser("new-endpoint", help="Query list of registered tokens")
        tokens.add_argument("-t", "--token-address", required=False, help="For the given token address")
        tokens.set_defaults(func=parser_function)


    def parser_function(args: Namespace) -> str:
        client = Client(endpoint=args.endpoint, version=args.version)
        tokens = client.new_endpoint(token_address=args.token_address)
        return utils.print_stdout(tokens)


5. Register CLI command at **raiden_client.interfaces.cli.CLI_ENDPOINTS**

.. code-block:: python

    CLI_ENDPOINTS = [
        ...
        "raiden_client.interfaces.cli_commands.new_endpoint",
        ...
    ]

5. Write corresponding test to be sure that interface interact in
expected way (regarding raiden api docs)

6. Run linters

.. code-block:: shell

    $ isort . --recursive -c -l 120 --skip venv/
    $ flake8 . --exclude=venv/
    $ pytest --cov=./raiden_client --cov-fail-under=100
