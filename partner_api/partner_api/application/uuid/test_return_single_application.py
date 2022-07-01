#  pytest -c "DEV" -s -v -m <test_name> --disable-pytest-warnings

import sys
import pytest
import json

from . import get_return_single_application_client
from partner_api.partner_api.auth import test_generate_access_token

# import config
from partner_api.partner_api import partner_api_config


# set up config
@pytest.fixture(autouse=True)
def set_env():
    env = sys.argv[2]
    print("\nEnv is " + env)
    get_return_single_application_client.config = partner_api_config.CONF.get(env)


@pytest.mark.sanity
@pytest.mark.positive
@pytest.mark.test_get_return_single_application_positive_etalon
def test_get_return_single_application_positive_etalon():
    """
    Positive case: get single application with etalon uuid
    """

    # get access token
    token = test_generate_access_token.test_generate_access_token_positive()

    uuid = get_return_single_application_client.config.get("uuid").get("etalon_uuid")

    test_response = get_return_single_application_client.get_return_single_applications(token, uuid)
    parse_json = json.loads(json.dumps(test_response.json()))

    assert test_response.status_code is 200
    assert parse_json["status"] == 'success'
    # add more asserts later


@pytest.mark.test_get_return_single_application_positive_param
def test_get_return_single_application_positive_param(uuid):
    """
    Positive case: get single application with parametrized uuid for use in other tests
    """

    # get access token
    token = test_generate_access_token.test_generate_access_token_positive()

    test_response = get_return_single_application_client.get_return_single_applications(token, uuid)
    parse_json = json.loads(json.dumps(test_response.json()))

    assert test_response.status_code is 200
    assert parse_json["status"] == 'success'
    # add more asserts later

    # return response for future use
    return test_response
