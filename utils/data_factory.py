from datetime import date, timedelta

from faker import Faker

fake = Faker()


def build_booking():
    checkin = date.today() + timedelta(days=30)
    checkout = checkin + timedelta(days=4)
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=100, max=900),
        "depositpaid": True,
        "bookingdates": {
            "checkin": checkin.isoformat(),
            "checkout": checkout.isoformat(),
        },
        "additionalneeds": "Breakfast",
    }