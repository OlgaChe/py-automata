import json

import allure
import pytest

import learning_service_client


@allure.step("Positive case: Check get example")
@pytest.mark.sanity
@pytest.mark.test_positive
def test_get_example_positive():
    """
    If all data is valid - test passes
    """
    test_response = learning_service_client.get_example()
    parse_json = json.loads(json.dumps(test_response.json()))
    assert test_response.status_code is 200
    assert "firstname" in parse_json
    assert parse_json["firstname"] == "John"


@allure.step("Fail example case: Check get example")
@pytest.mark.test_fail
def test_get_example_fail():
    """
    Wrong assert to see failed test
    """
    test_response = learning_service_client.get_example()
    parse_json = json.loads(json.dumps(test_response.json()))
    assert test_response.status_code is 200
    assert parse_json["firstname"] == "Jane"


@pytest.mark.sanity
def test_get_example_params():
    test_response = learning_service_client.get_example_params()
    assert test_response.status_code is 200


@pytest.mark.sanity
@pytest.mark.parametrize("lat", [50])
@pytest.mark.parametrize("lon", [20])
def test_get_example_parametrized(lat, lon):
    test_response = learning_service_client.get_example_parametrized(lat, lon)
    assert test_response.status_code is 200


@pytest.mark.sanity
def test_get_example_config():
    test_response = learning_service_client.get_example_config()
    assert test_response.status_code is 200


@pytest.mark.sanity
def test_post_example():
    test_response = learning_service_client.get_example()
    assert test_response.status_code is 200


@pytest.mark.sanity
def test_post_json_example():
    test_response = learning_service_client.post_example_json_file()
    assert test_response.status_code is 200
