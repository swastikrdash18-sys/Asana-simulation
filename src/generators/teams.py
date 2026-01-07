import uuid
from utils.dates import random_past_datetime

TEAMS = [
    ("Backend Engineering", "Engineering"),
    ("Frontend Engineering", "Engineering"),
    ("Product Management", "Product"),
    ("Growth Marketing", "Marketing"),
    ("Platform Operations", "Operations")
]

def generate_teams(cursor, organization_id):
    team_ids = []
    for name, dept in TEAMS:
        team_id = str(uuid.uuid4())
        cursor.execute(
            "INSERT INTO teams VALUES (?, ?, ?, ?, ?)",
            (team_id, organization_id, name, dept, random_past_datetime(1500))
        )
        team_ids.append(team_id)
    return team_ids