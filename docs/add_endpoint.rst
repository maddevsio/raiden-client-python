Implement Raiden API endpoint
=============================

In case if Raiden API add new endpoint client should implement following stuff:

Create new endpoint interface
--------------------------------

1. Create new endpoint at **raiden_client/endpoints/**

2. Implement Request Object

.. code-block:: python

    class NewAPIRequest(BaseRequest):
        """Title.

        Description

        GET /api/(version)/address
        https://raiden-network.readthedocs.io/en/latest/rest_api.html#address
        """

        @property
        def endpoint(self) -> str:
            return "/address"

        @property
        def method(self) -> str:
            return "get"

        def payload(self) -> Dict[str, Any]:
            return {}


3. Implement Response Object

.. code-block:: python

    class NewAPIResponse(BaseResponse):

        def __init__(self, our_address: Address):
            self.our_address = our_address

        @classmethod
        def from_dict(cls, d: Dict[str, Any]) -> BaseResponse:
            return cls(**d)

        def to_dict(self) -> Dict[str, str]:
            return {"our_address": self.our_address}


Add new method to Client interface
----------------------------------

.. code-block:: python

    def channels(self, token_address: Address = None) -> List[ChannelType]:
        """Get a list of all unsettled channels.

        :params: token_address (optional) (str)
        :returns: List of channels
        """
        request = ChannelsRequest()
        api_response = self.handler.do(request)
        response = ChannelsResponse.from_dict(api_response)
        return response.to_dict()

Add new CLI subparser
---------------------

Add to create_subparser() function:


Add doc string and meaningful cli parameters description

.. code-block:: python

    tokens = subparsers.add_parser("tokens", help="")
    tokens.add_argument("-t", "--token-address", required=False, help="")
    tokens.set_defaults(func=tokens_func)


Implement parser function function:

.. code-block:: python

    def tokens_func(client: Client, args: argparse.Namespace) -> None:
        tokens = client.tokens(token_address)
        print(json.dumps(tokens, indent=2))
