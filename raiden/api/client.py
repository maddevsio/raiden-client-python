

class Client:
    """Main Client APP.

    Communicate with API via client class.
    """

    def __init__(self, endpoint: str, version: str = "v1") -> None:
        self.endpoint = endpoint
        self.version = version
