import sys

from . import get_return_list_of_applications_client

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
    get_return_list_of_applications_client.config = partner_api_config.CONF.get(env)


@pytest.mark.parametrize('filter_param', ["test"])
@pytest.mark.parametrize('limit', [20])
@pytest.mark.parametrize('page', [2])
@pytest.mark.parametrize('direction', ["desc"])
@pytest.mark.parametrize('sort', ["requested_funding"])
@pytest.mark.sanity
@pytest.mark.positive
@pytest.mark.test_get_return_list_of_applications_client_positive
def test_get_return_list_of_applications_client_positive(filter_param, limit, page, direction, sort):
    """
    Positive case: get lisf of applications
    """

    token = '3bedf587d3b21eaad83d667e1cf05712314f713a82feb492f681c5b6139ce3a8'

    test_response = get_return_list_of_applications_client.get_return_list_of_applications(token, filter_param, limit, page, direction, sort)
    parse_json = json.loads(json.dumps(test_response.json()))

    assert test_response.status_code is 200
    assert parse_json["status"] == 'success'
    # add more asserts later
