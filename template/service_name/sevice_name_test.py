import allure
import pytest


@allure.step("Positive case: ")
@pytest.mark.sanity
@pytest.mark.test_service_name
@pytest.mark.testpositive
@pytest.mark.test_service_name_positive
@pytest.mark.parametrize()
def test_service_name_positive():
    """
    If all data is valid - test passes
    """
    paramparam = CONF.get().get("param_positive")
    test_response = grpc_client.client_request_name(paramparam=paramparam)
    assert "success: true" in test_response
    assert "error" not in test_response


@allure.step("Negative case: ")
@pytest.mark.test_service_name
@pytest.mark.testnegative
@pytest.mark.test_service_name_negative
@pytest.mark.parametrize()
def test_service_name_negative():
    """
    Negative case:
    """
    paramparam = CONF.get().get("param_neg")
    test_response = grpc_client.client_request_name(paramparam=paramparam)
    assert 'error: ' in test_response
