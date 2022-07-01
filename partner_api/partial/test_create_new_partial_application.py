#  pytest -c "DEV" -s -v -m <test_name> --disable-pytest-warnings

import sys
import pytest
import json

from . import post_create_new_partial_application_client
from partner_api.auth import test_generate_access_token

# import config
from .. import partner_api_config


# set up config
@pytest.fixture(autouse=True)
def set_env():
    env = sys.argv[2]
    print("\nEnv is " + env)
    post_create_new_partial_application_client.config = partner_api_config.CONF.get(env)


# Creates a new partial application.
# Fields required in the full application endpoint are necessary for underwriting.
# Fewer fields are required for partial submissions.
# However, a partial submission will only be submitted to underwriting once all necessary
# POST {{baseUrl}}/partial
# positive case
@pytest.mark.parametrize('new_application_json', ["partial/sanity_test/post_create_new_partial_application.json"])
@pytest.mark.sanity
@pytest.mark.positive
@pytest.mark.test_post_create_new_partial_application_positive
def test_post_create_new_partial_application_positive(new_application_json):
    """
    Positive case: create new partial application with valid data
    """

    # get access token
    token = test_generate_access_token.test_generate_access_token_positive()

    test_response = post_create_new_partial_application_client.post_create_new_partial_application(token, new_application_json)
    parse_json = json.loads(json.dumps(test_response.json()))

    assert test_response.status_code is 200
    assert parse_json["kapitus_application_status"] == "Approved"
    assert parse_json["uuid"] != ""
    assert parse_json["offer_link"] != ""

    # get uuid
    uuid = parse_json["uuid"]
    print(uuid)

    # return uuid for future use
    return uuid

