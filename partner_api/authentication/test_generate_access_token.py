import generate_access_token_client

# import auth config
from auth_config import CONF

import pytest
import allure
import json


# positive case
@allure.step("Positive case: Success auth")
@pytest.mark.sanity
def generate_access_token(client_id, client_secret):
    test_response = generate_access_token_client.generate_access_token(CONF.get("auth").get("client_id"),
                                                                       CONF.get("auth").get("client_secret"))
    parse_json = json.loads(json.dumps(test_response.json()))

    assert test_response.status_code is 200
    assert parse_json.status == "success"
    assert parse_json.data.access_token is not None
