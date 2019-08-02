Implement Raiden API endpoint
=============================

In case if Raiden API add new endpoint client should implement following stuff:

Create new endpoint interface
--------------------------------

1. Create new plugin at **raiden_client/plugin/**

2. Implement Plugin interface

.. code-block:: python

    class TokensPlugin(BasePlugin):
        """Registers a token.
        If a token is not registered yet (i.e.: A token network for that token does not exist in the registry),
        we need to register it by deploying a token network contract for that token.

        PUT /api/(version)/tokens/(token_address)
        Doc: https://raiden-network.readthedocs.io/en/latest/rest_api.html#deploying
        """
        tokens = None

        def __init__(self, token_address: str = None) -> None:
            self.token_address = self._normalize_address(token_address)

        @property
        def name(self) -> str:
            return "tokens"

        @property
        def endpoint(self) -> str:
            return "/tokens"

        @property
        def method(self) -> str:
            return "get"

        def payload(self) -> Dict[str, Any]:
            return {}

        def parse_response(self, response) -> Dict[str, Any]:
            self.tokens = response

        def to_dict(self):
            return {"tokens": self.tokens}

        @classmethod
        def configure_parser(cls, arg_parser: ArgumentParser, subparser: _SubParsersAction) -> None:
            tokens = subparser.add_parser("tokens", help="Query list of registered tokens")
            tokens.add_argument("-t", "--token-address", required=False, help="For the given token address")
            tokens.set_defaults(func=cls.plugin_execute)

        @classmethod
        def plugin_execute(cls, args: Namespace) -> None:
            plugin = cls(args.token_address)
            output = plugin.raiden_node_api_interact(args.endpoint)
            print(json.dumps(output, indent=2))


3. Register new plugin **raiden_client/plugins/register.py** at **CLIENT_PLUGINS_V1**


4. Add new method at Client interface: **raiden_client/interfaces/client.py**

.. code-block:: python

    def tokens(self, token_address: str = None) -> List[str]:
        """Returns a list of addresses of all registered tokens.

        :params: token_address (address) (optional) Returns the address of token network for the given token
        :returns: list of addresses (or address if toke_address param passed)
        """
        plugin = TokensPlugin(token_address=token_address)
        return plugin.raiden_node_api_interact(self.endpoint)

5. Write corresponding test to be sure that interface interact in expected way (regarding raiden api docs)
