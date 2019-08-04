from unittest import mock

import requests

from raiden_client.interfaces.cli import create_main_parser
from raiden_client.interfaces.cli_commands.address import configure_parser


@mock.patch.object(requests, 'request')
def test_address_cli_command(mocked) -> None:
    mockresponse = mocked.Mock()
    mocked.return_value = mockresponse
    mockresponse.status_code = 200
    mockresponse.text = "OK"

    def json():
        return {"our_address": "0x123"}

    mockresponse.json = json

    main_parser = create_main_parser()
    subparsers = main_parser.add_subparsers()
    configure_parser(main_parser, subparsers)

    args = main_parser.parse_args(["address"])
    assert hasattr(args, "func")
    assert args.func(args)
