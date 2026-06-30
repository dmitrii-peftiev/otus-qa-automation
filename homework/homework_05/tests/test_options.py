import pytest
import requests


@pytest.mark.homework_05_options
def test_api_status(url, status):
    response = requests.get(url)
    assert response.status_code == status
