import uuid
from faker import Faker
from utils.dates import random_past_datetime

fake = Faker()

DEPARTMENTS = ["Engineering", "Product", "Marketing", "Operations"]
ROLES = ["Engineer", "Senior Engineer", "Manager", "Lead", "Analyst"]

def generate_users(cursor, organization_id, n=50):
    """
    n=50 for now (small number for testing).
    We'll scale to thousands later.
    """
    user_ids = []

    for _ in range(n):
        user_id = str(uuid.uuid4())
        cursor.execute(
            "INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                user_id,
                organization_id,
                fake.name(),
                fake.unique.email(),
                fake.random_element(ROLES),
                fake.random_element(DEPARTMENTS),
                random_past_datetime(1200)
            )
        )
        user_ids.append(user_id)

    return user_ids