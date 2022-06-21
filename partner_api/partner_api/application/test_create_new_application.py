import sys

from . import post_create_new_application_client

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
    post_create_new_application_client.config = partner_api_config.CONF.get(env)


# Creates a new application
# POST {{baseUrl}}/application
# positive case
@pytest.mark.parametrize('new_application_json', ["partner_api/application/sanity_test/post_create_new_application.json"])
@pytest.mark.sanity
@pytest.mark.positive
@pytest.mark.test_post_create_new_application_positive
def test_post_create_new_application_positive(new_application_json):
    """
    Positive case: create new full application with valid data
    """

    token = '3bedf587d3b21eaad83d667e1cf05712314f713a82feb492f681c5b6139ce3a8'

    test_response = post_create_new_application_client.post_create_new_application(token, new_application_json)
    parse_json = json.loads(json.dumps(test_response.json()))

    assert test_response.status_code is 200
    assert parse_json["kapitus_application_status"] == "Approved"
    assert parse_json["uuid"] != ""
    assert parse_json["offer_link"] != ""

    print(parse_json["uuid"])
    return parse_json["uuid"]

