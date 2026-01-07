import uuid
import random
from utils.dates import random_past_datetime, random_future_date, avoid_weekends

TASK_TEMPLATES = [
    "Fix authentication bug",
    "Improve API latency",
    "Prepare marketing assets",
    "Update onboarding flow",
    "Refactor payment service",
    "Write campaign copy"
]

def generate_tasks(cursor, project_ids, section_map, user_ids, n_per_project=10):
    """
    Generates realistic tasks per project and RETURNS task_ids.
    """
    task_ids = []

    for project_id in project_ids:
        for _ in range(n_per_project):
            task_id = str(uuid.uuid4())
            section_id = random.choice(section_map[project_id])

            assignee_id = (
                random.choice(user_ids) if random.random() > 0.15 else None
            )

            created_at = random_past_datetime(365)
            completed = random.random() < 0.6
            completed_at = created_at if completed else None

            due_date = (
                avoid_weekends(random_future_date())
                if random.random() > 0.1 else None
            )

            cursor.execute(
                "INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    task_id,
                    project_id,
                    section_id,
                    assignee_id,
                    random.choice(TASK_TEMPLATES),
                    None,
                    due_date,
                    created_at,
                    completed,
                    completed_at
                )
            )

            task_ids.append(task_id)

    return task_ids