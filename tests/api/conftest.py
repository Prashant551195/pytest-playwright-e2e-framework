import pytest

from api import booking_client


@pytest.fixture(scope="session")
def token():
    response = booking_client.create_token()
    assert response.status_code == 200
    return response.json()["token"]