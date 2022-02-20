import generate_access_token_client

# import auth config
from auth_config import CONF

import pytest
import json


# positive case
@pytest.mark.sanity
def test_generate_access_token():
    """
    Positive case: Success auth
    """

    test_response = generate_access_token_client.generate_access_token(CONF.get("auth").get("client_id"),
                                                                       CONF.get("auth").get("client_secret"))
    parse_json = json.loads(json.dumps(test_response.json()))

    assert test_response.status_code is 200
    assert parse_json["status"] == "success"
    assert parse_json["data"]["access_token"] != ""

    print(parse_json["data"]["access_token"] )


# positive case
@pytest.mark.sanity
def test_generate_access_token_negative():
    """
    Positive case: Success auth
    """

    test_response = generate_access_token_client.generate_access_token(CONF.get("auth").get("client_id_neg"),
                                                                       CONF.get("auth").get("client_secret_neg"))
    parse_json = json.loads(json.dumps(test_response.json()))

    assert test_response.status_code is not 200
    assert parse_json["status"] == "forbidden"
    assert parse_json["data"] == "Invalid pair client_id and client_secret"
