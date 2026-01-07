import uuid
from utils.dates import random_past_datetime

def generate_organization(cursor):
    org_id = str(uuid.uuid4())
    cursor.execute(
        "INSERT INTO organizations VALUES (?, ?, ?, ?)",
        (org_id, "NovaCloud Technologies", "novacloud.com", random_past_datetime(2000))
    )
    return org_id