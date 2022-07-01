#  pytest -c "DEV" -s -v -m <test_name> --disable-pytest-warnings

from datetime import datetime
import random
import sys
import pytest
import json

from . import put_update_partial_application_client
from partner_api.auth import test_generate_access_token
# from partner_api.partner_api.application.uuid import test_return_single_application

# import config
from .. import partner_api_config


# set up config
@pytest.fixture(autouse=True)
def set_env():
    env = sys.argv[2]
    print("\nEnv is " + env)
    put_update_partial_application_client.config = partner_api_config.CONF.get(env)


# Update an partial application
# POST {{baseUrl}}/partial
# positive case
@pytest.mark.parametrize('update_application_json', ["partial/sanity_test/post_create_new_partial_application.json"])
@pytest.mark.sanity
@pytest.mark.positive
@pytest.mark.test_put_update_partial_application_positive_etalon_all_required_data
def test_put_update_partial_application_positive_etalon_all_required_data(update_application_json):
    """
    Positive case: update partial application with valid data
    """

    # get access token
    token = test_generate_access_token.test_generate_access_token_positive()

    uuid = put_update_partial_application_client.config.get("uuid").get("etalon_uuid_edit")

    with open(update_application_json) as json_file:
        json_data = json.load(json_file)
        json_data["owners"][0]["first_name"] = "qa_" + datetime.now().strftime('%m%d%y%H%M%S') + "_FN"
        json_data["owners"][0]["last_name"] = "qa_" + datetime.now().strftime('%m%d%y%H%M%S') + "_LN"
        json_data["owners"][0]["phonenumbers"][0]["number"] = "212" + str(random.randint(0, 9999999)).zfill(10)
        json_data["owners"][0]["emails"][0]["email"] = "email_owner+" + datetime.now().strftime('%m%d%y%H%M%S') + "@example.com"

    test_response = put_update_partial_application_client.put_update_partial_application(token, json_data, uuid)
    parse_json = json.loads(json.dumps(test_response.json()))

    assert test_response.status_code is 200
    assert parse_json["kapitus_application_status"] == "Approved"
    assert parse_json["uuid"] != ""
    assert parse_json["uuid"] == uuid
    assert parse_json["offer_link"] != ""

    # return uuid for future use
    print(parse_json["uuid"])
    return parse_json["uuid"]

