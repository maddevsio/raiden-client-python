Implement Raiden API endpoint
=============================

In case if Raiden API add new endpoint client should implement following steps:


Create new endpoint interface
--------------------------------

1. Create new plugin file at **raiden_client/plugins/**

2. Implement BaseEndpoint interface

.. code-block:: python

    class Address(BaseEndpoint):
        """Querying Information About Your Raiden Node"""
        # TODO: Describe each method/parameter
        our_address = None

        @property
        def name(self) -> str:
            return "address"

        @property
        def endpoint(self) -> str:
            return "/address"

        @property
        def method(self) -> str:
            return "get"

        def payload(self) -> Dict[str, Any]:
            return {}

        def from_dict(self, response: Dict[str, Any]) -> None:
            self.our_address = response["our_address"]

        def to_dict(self) -> Dict[str, str]:
            return {"our_address": self.our_address}



3. Add new method at Client interface: **raiden_client/interfaces/client.py**

.. code-block:: python

    def address(self) -> Dict[str, str]:
        """Query your address."""
        endpoint = Address()
        return self.raiden_api.request(endpoint)

4. Create new command at raiden_client/interfaces/cli_commands/

.. code-block:: python

    def configure_parser(arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
        address = subparser.add_parser("address", help="Query node address")
        address.set_defaults(func=parser_function)


    def parser_function(args: Namespace) -> Dict[str, str]:
        c = Client()
        return c.address()

5. Write corresponding test to be sure that interface interact in
expected way (regarding raiden api docs)
