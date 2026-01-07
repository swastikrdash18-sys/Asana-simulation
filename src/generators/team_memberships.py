import random
from utils.dates import random_past_datetime

def generate_team_memberships(cursor, team_ids, user_ids):
    """
    Each user belongs to 1–2 teams (realistic matrix org).
    """
    for user_id in user_ids:
        for team_id in random.sample(team_ids, random.randint(1, 2)):
            cursor.execute(
                "INSERT INTO team_memberships VALUES (?, ?, ?)",
                (team_id, user_id, random_past_datetime(1000))
            )