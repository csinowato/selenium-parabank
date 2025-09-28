import uuid


class TestData:
    # login credentials
    VALID_USER = {"username": "john", "password": "demo"}

    # generate sample user with unique username
    @staticmethod
    def sample_user():
        return {
            "first_name": "Test",
            "last_name": "User",
            "address": "123 Test St",
            "city": "Test City",
            "state": "NY",
            "zip_code": "12345",
            "phone": "555-1234",
            "ssn": "123-45-6789",
            "username": f"user_{uuid.uuid4().hex[:6]}",
            "password": "password123",
            "confirm_password": "password123",
        }

    # sample payee data
    ELECTRIC_COMPANY = {
        "name": "Electric Company",
        "address": "123 Power St",
        "city": "Energy City",
        "state": "CA",
        "zip_code": "54321",
        "phone": "555-POWER",
    }
