import pytest
from homework.homework_05.tests.api_client import APIClient

pytestmark = pytest.mark.homework_05_all

client = APIClient("https://api.openbrewerydb.org/v1/breweries")


def test_get_breweries_list():
    response = client.get("")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.parametrize(
    "brewery_id",
    [pytest.param("21f21cc0-5b2f-4b79-be29-3bc625bcc4c8", id="brewery_id")],
)
def test_get_single_brewery(brewery_id):
    response = client.get(f"/{brewery_id}")
    assert response.status_code == 200
    assert response.json()["id"] == brewery_id


@pytest.mark.parametrize(
    "country",
    [
        pytest.param("Germany", id="country_germany"),
        pytest.param("Belgium", id="country_belgium"),
    ],
)
def test_filter_breweries_by_country(country):
    response = client.get("", params={"by_country": country})
    assert response.status_code == 200
    for brewery in response.json():
        assert country in brewery["country"]


@pytest.mark.parametrize(
    "size",
    [pytest.param(3, id="limit_3_items"), pytest.param(10, id="limit_10_items")],
)
def test_breweries_pagination(size):
    response = client.get("", params={"per_page": size})
    assert response.status_code == 200
    assert len(response.json()) == size


def test_search_breweries():
    response = client.get("/search", params={"query": "Weihenstephan"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
