import requests

from config.settings import API_BASE_URL

HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}
TIMEOUT = 30


def create_token(username="admin", password="password123"):
    return requests.post(
        f"{API_BASE_URL}/auth",
        json={"username": username, "password": password},
        headers=HEADERS,
        timeout=TIMEOUT,
    )


def create_booking(data):
    return requests.post(
        f"{API_BASE_URL}/booking",
        json=data,
        headers=HEADERS,
        timeout=TIMEOUT,
    )


def get_booking(booking_id):
    return requests.get(
        f"{API_BASE_URL}/booking/{booking_id}",
        headers=HEADERS,
        timeout=TIMEOUT,
    )


def update_booking(booking_id, data, token):
    return requests.put(
        f"{API_BASE_URL}/booking/{booking_id}",
        json=data,
        headers={**HEADERS, "Cookie": f"token={token}"},
        timeout=TIMEOUT,
    )


def delete_booking(booking_id, token):
    return requests.delete(
        f"{API_BASE_URL}/booking/{booking_id}",
        headers={**HEADERS, "Cookie": f"token={token}"},
        timeout=TIMEOUT,
    )