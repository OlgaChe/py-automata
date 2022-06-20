import sys

from . import generate_access_token_client

import pytest
import json

# import config
from partner_api.partner_api import partner_api_config

#  pytest -c "DEV" -s -v -m <test_name> --disable-pytest-warnings


# set up config
@pytest.fixture(autouse=True)
def set_env():
    env = sys.argv[2]
    print("\nEnv is " + env)
    generate_access_token_client.config = partner_api_config.CONF.get(env)


# positive case
@pytest.mark.sanity
def test_generate_access_token():
    """
    Positive case: Success auth
    """

    test_response = generate_access_token_client.generate_access_token(
        generate_access_token_client.config.get("auth").get("client_id"),
        generate_access_token_client.config.get("auth").get("client_secret"))
    parse_json = json.loads(json.dumps(test_response.json()))

    assert test_response.status_code is 200
    assert parse_json["status"] == "success"
    assert parse_json["data"]["access_token"] != ""

    print(parse_json["data"]["access_token"] )


# positive case
@pytest.mark.sanity
def test_generate_access_token_negative():
    """
    Negative case: Forbidden status
    """

    test_response = generate_access_token_client.generate_access_token(
        generate_access_token_client.config.get("auth").get("client_id_neg"),
        generate_access_token_client.config.get("auth").get("client_secret_neg"))
    parse_json = json.loads(json.dumps(test_response.json()))

    assert test_response.status_code is not 200
    assert parse_json["status"] == "forbidden"
    assert parse_json["data"] == "Invalid pair client_id and client_secret"
