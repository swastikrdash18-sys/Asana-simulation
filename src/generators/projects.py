import uuid
from utils.dates import random_past_datetime

PROJECT_TEMPLATES = [
    ("Auth Revamp Sprint", "Sprint"),
    ("Q3 Marketing Campaign", "Campaign"),
    ("Payments Roadmap", "Roadmap"),
    ("Infra Reliability", "Operations")
]

def generate_projects(cursor, organization_id, team_ids):
    project_ids = []

    for team_id in team_ids:
        for name, ptype in PROJECT_TEMPLATES:
            project_id = str(uuid.uuid4())
            cursor.execute(
                "INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    project_id,
                    organization_id,
                    team_id,
                    name,
                    ptype,
                    None,
                    None,
                    random_past_datetime(900)
                )
            )
            project_ids.append(project_id)

    return project_ids