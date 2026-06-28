import pytest
from homework.homework_05.tests.api_client import APIClient

pytestmark = pytest.mark.homework_05_all

client = APIClient("https://dog.ceo/api")


def test_get_random_dog():
    response = client.get("/breeds/image/random")
    assert response.status_code == 200
    assert "message" in response.json()


def test_get_all_breeds():
    response = client.get("/breeds/list/all")
    assert response.status_code == 200
    assert response.json()["status"] == "success"


@pytest.mark.parametrize(
    "breed",
    [
        pytest.param("husky", id="husky_breed"),
        pytest.param("corgi", id="corgi_breed"),
        pytest.param("german", id="german_breed"),
    ],
)
def test_get_breed_images(breed):
    response = client.get(f"/breed/{breed}/images")
    assert response.status_code == 200
    assert isinstance(response.json()["message"], list)


@pytest.mark.parametrize(
    "breed, sub",
    [
        pytest.param("corgi", "cardigan", id="corgi_cardigan"),
        pytest.param("german", "shepherd", id="german_shepherd"),
    ],
)
def test_get_sub_breed(breed, sub):
    response = client.get(f"/breed/{breed}/{sub}/images")
    assert response.status_code == 200


@pytest.mark.parametrize(
    "invalid",
    [
        pytest.param("cat", id="invalid_breed_cat"),
        pytest.param(None, id="invalid_breed_none"),
    ],
)
def test_invalid_breed(invalid):
    response = client.get(f"/breed/{invalid}/images")
    assert response.status_code == 404
    assert response.json()["status"] == "error"
