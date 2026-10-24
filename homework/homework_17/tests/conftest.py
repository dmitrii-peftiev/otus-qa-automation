import pymysql
import pytest


def pytest_addoption(parser):
    parser.addoption("--host", action="store", default="127.0.0.1")
    parser.addoption("--port", action="store", default="3306")
    parser.addoption("--database", action="store", default="prestashop")
    parser.addoption("--user", action="store", default="root")
    parser.addoption("--password", action="store", default="admin")


@pytest.fixture(scope="session")
def connection(request):
    host = request.config.getoption("--host")
    port = int(request.config.getoption("--port"))
    database = request.config.getoption("--database")
    user = request.config.getoption("--user")
    password = request.config.getoption("--password")

    conn = pymysql.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password,
        cursorclass=pymysql.cursors.DictCursor,
    )
    yield conn
    conn.close()
