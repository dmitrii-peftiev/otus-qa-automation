import time

import pytest

from homework.homework_17.src import db

pytestmark = pytest.mark.homework_17


@pytest.fixture
def unique_email():
    return f"test_user_{int(time.time())}@example.com"


def test_create_customer(connection, unique_email):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    customer_data = {
        "firstname": "Test",
        "lastname": "User",
        "email": unique_email,
        "passwd": "password123",
        "secure_key": "key123",
        "active": 1,
        "id_gender": 1,
        "date_add": current_time,
        "date_upd": current_time,
    }

    customer_id = db.create_customer(connection, customer_data)
    assert customer_id > 0

    res = db.get_customer_by_id(connection, customer_id)
    assert res is not None
    assert res["firstname"] == "Test"
    assert res["lastname"] == "User"
    assert res["email"] == unique_email


def test_update_existing_customer(connection, unique_email):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    customer_data = {
        "firstname": "Test",
        "lastname": "User",
        "email": unique_email,
        "passwd": "password123",
        "secure_key": "key123",
        "active": 1,
        "id_gender": 1,
        "date_add": current_time,
        "date_upd": current_time,
    }
    customer_id = db.create_customer(connection, customer_data)

    new_email = f"updated_user_{int(time.time())}@example.com"
    update_time = time.strftime("%Y-%m-%d %H:%M:%S")
    update_data = {
        "firstname": "Updated",
        "lastname": "Tester",
        "email": new_email,
        "date_upd": update_time,
    }

    affected = db.update_customer(connection, customer_id, update_data)
    assert affected == 1

    res = db.get_customer_by_id(connection, customer_id)
    assert res["firstname"] == "Updated"
    assert res["lastname"] == "Tester"
    assert res["email"] == new_email


def test_update_non_existing_customer(connection):
    update_time = time.strftime("%Y-%m-%d %H:%M:%S")
    update_data = {
        "firstname": "Updated",
        "lastname": "Tester",
        "email": "test@example.com",
        "date_upd": update_time,
    }
    affected = db.update_customer(connection, 999999, update_data)
    assert affected == 0


def test_delete_existing_customer(connection, unique_email):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    customer_data = {
        "firstname": "Test",
        "lastname": "User",
        "email": unique_email,
        "passwd": "password123",
        "secure_key": "key123",
        "active": 1,
        "id_gender": 1,
        "date_add": current_time,
        "date_upd": current_time,
    }
    customer_id = db.create_customer(connection, customer_data)

    affected = db.delete_customer(connection, customer_id)
    assert affected == 1

    res = db.get_customer_by_id(connection, customer_id)
    assert res is None


def test_delete_non_existing_customer(connection):
    affected = db.delete_customer(connection, 999999)
    assert affected == 0
