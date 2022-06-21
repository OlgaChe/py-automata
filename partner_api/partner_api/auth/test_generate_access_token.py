import sys

from . import get_generate_access_token_client

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
    get_generate_access_token_client.config = partner_api_config.CONF.get(env)


# Generates an Access Token
# GET {{baseUrl}}/authenticate
# positive case
@pytest.mark.sanity
@pytest.mark.positive
@pytest.mark.test_generate_access_token_positive_positive
def test_generate_access_token_positive():
    """
    Positive case: Success auth
    """

    test_response = get_generate_access_token_client.get_generate_access_token(
        get_generate_access_token_client.config.get("auth").get("client_id"),
        get_generate_access_token_client.config.get("auth").get("client_secret"))
    parse_json = json.loads(json.dumps(test_response.json()))

    assert test_response.status_code is 200
    assert parse_json["status"] == "success"
    assert parse_json["data"]["access_token"] != ""

    print(parse_json["data"]["access_token"])
    return parse_json["data"]["access_token"]


# negative case
@pytest.mark.sanity
@pytest.mark.negative
@pytest.mark.test_generate_access_token_negative
def test_generate_access_token_negative():
    """
    Negative case: Forbidden status
    """

    test_response = get_generate_access_token_client.get_generate_access_token(
        get_generate_access_token_client.config.get("auth").get("client_id_neg"),
        get_generate_access_token_client.config.get("auth").get("client_secret_neg"))
    parse_json = json.loads(json.dumps(test_response.json()))

    assert test_response.status_code is not 200
    assert parse_json["status"] == "forbidden"
    assert parse_json["data"] == "Invalid pair client_id and client_secret"
