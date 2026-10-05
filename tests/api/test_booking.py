import pytest

from api import booking_client
from utils.data_factory import build_booking

pytestmark = pytest.mark.api


def test_create_token(token):
    assert token


def test_create_booking():
    data = build_booking()
    response = booking_client.create_booking(data)
    assert response.status_code == 200
    body = response.json()
    assert "bookingid" in body
    assert body["booking"]["firstname"] == data["firstname"]
    assert body["booking"]["lastname"] == data["lastname"]


def test_get_booking():
    data = build_booking()
    booking_id = booking_client.create_booking(data).json()["bookingid"]
    response = booking_client.get_booking(booking_id)
    assert response.status_code == 200
    assert response.json()["firstname"] == data["firstname"]
    assert response.json()["totalprice"] == data["totalprice"]


def test_update_booking(token):
    booking_id = booking_client.create_booking(build_booking()).json()["bookingid"]
    new_data = build_booking()
    response = booking_client.update_booking(booking_id, new_data, token)
    assert response.status_code == 200
    assert response.json()["firstname"] == new_data["firstname"]


def test_delete_booking(token):
    booking_id = booking_client.create_booking(build_booking()).json()["bookingid"]
    response = booking_client.delete_booking(booking_id, token)
    assert response.status_code == 201


def test_booking_lifecycle(token):
    data = build_booking()
    booking_id = booking_client.create_booking(data).json()["bookingid"]

    assert booking_client.get_booking(booking_id).status_code == 200

    new_data = build_booking()
    updated = booking_client.update_booking(booking_id, new_data, token)
    assert updated.json()["lastname"] == new_data["lastname"]

    assert booking_client.delete_booking(booking_id, token).status_code == 201
    assert booking_client.get_booking(booking_id).status_code == 404