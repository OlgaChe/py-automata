#  pytest -c "DEV" -s -v -m <test_name> --disable-pytest-warnings

import sys
import pytest
import json

from . import get_return_list_of_applications_client
from partner_api.auth import test_generate_access_token

# import config
from .. import partner_api_config


# set up config
@pytest.fixture(autouse=True)
def set_env():
    env = sys.argv[2]
    print("\nEnv is " + env)
    get_return_list_of_applications_client.config = partner_api_config.CONF.get(env)


@pytest.mark.parametrize('filter_param', [None])
@pytest.mark.parametrize('limit', [20])
@pytest.mark.parametrize('page', [2])
@pytest.mark.parametrize('direction', ["desc"])
@pytest.mark.parametrize('sort', ["requested_funding"])
@pytest.mark.sanity
@pytest.mark.positive
@pytest.mark.test_get_return_list_of_applications_positive
def test_get_return_list_of_applications_positive(filter_param, limit, page, direction, sort):
    """
    Positive case: get lisf of applications
    """

    # get access token
    token = test_generate_access_token.test_generate_access_token_positive()

    test_response = get_return_list_of_applications_client.get_return_list_of_applications(token, filter_param, limit, page, direction, sort)
    parse_json = json.loads(json.dumps(test_response.json()))

    assert test_response.status_code is 200
    assert parse_json["status"] == 'success'
    # add more asserts later
