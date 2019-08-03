Implement Raiden API endpoint
=============================

In case if Raiden API add new endpoint client should implement following steps:


Create new endpoint interface
--------------------------------

1. Create new plugin file at **raiden_client/plugins/**

2. Implement BaseEndpoint interface

.. code-block:: python

    class AddressEndpoint(BaseEndpoint):
        """Title

        Description

        Link to Raiden Rest API doc
        """

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

        def from_dict(self, response) -> Dict[str, Any]:
            if "our_address" in response:
                self.our_address = response["our_address"]

        def to_dict(self):
            return {"our_address": self.our_address}

        @classmethod
        def configure_parser(cls, arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
            address = subparser.add_parser("address", help="Query node address")
            address.set_defaults(func=cls.parser_function)

        @classmethod
        def parser_function(cls, args: Namespace) -> None:
            address = cls()
            address.raiden_node_api_interact(args.endpoint)
            output = address.to_dict()
            print(json.dumps(output["our_address"], indent=2))


3. Register new plugin **raiden_client/plugins/register.py**
at **CLIENT_PLUGINS_V1**


4. Add new method at Client interface: **raiden_client/interfaces/client.py**

.. code-block:: python

    def plugin_name(self, token_address: str = None) -> List[str]:
        """Returns a list of addresses of all registered tokens.

        :params: token_address (address) (optional) Returns the address of token network for the given token
        :returns: list of addresses (or address if toke_address param passed)
        """
        plugin = TokensEndpoint(token_address=token_address)
        return plugin.raiden_node_api_interact(self.endpoint)

5. Write corresponding test to be sure that interface interact in
expected way (regarding raiden api docs)
