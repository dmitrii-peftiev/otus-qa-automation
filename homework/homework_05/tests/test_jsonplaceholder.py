import pytest
from homework.homework_05.tests.api_client import APIClient

pytestmark = pytest.mark.homework_05_all

client = APIClient("https://jsonplaceholder.typicode.com")


def test_get_all_posts():
    response = client.get("/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.parametrize(
    "post_id",
    [
        pytest.param(1, id="first_post"),
        pytest.param(100, id="last_post"),
    ],
)
def test_get_single_post(post_id):
    response = client.get(f"/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id


def test_create_post():
    body = {"title": "corgi", "body": "cardigan", "userId": 1}
    response = client.post("/posts", json=body)
    assert response.status_code == 201
    assert response.json()["title"] == "corgi"


@pytest.mark.parametrize(
    "post_id",
    [
        pytest.param(1, id="update_post"),
    ],
)
def test_update_post(post_id):
    body = {
        "id": post_id,
        "title": "german",
        "body": "shepherd",
        "userId": 1,
    }
    response = client.put(f"/posts/{post_id}", json=body)
    assert response.status_code == 200
    assert response.json()["title"] == "german"


@pytest.mark.parametrize(
    "post_id",
    [
        pytest.param(1, id="delete_post"),
    ],
)
def test_delete_post(post_id):
    response = client.delete(f"/posts/{post_id}")
    assert response.status_code == 200
