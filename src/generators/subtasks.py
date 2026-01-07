import uuid
import random
from utils.dates import random_past_datetime

SUBTASK_TEMPLATES = [
    "Investigate issue",
    "Write unit tests",
    "Fix implementation",
    "Review changes",
    "Deploy to staging"
]

def generate_subtasks(cursor, task_ids, user_ids):
    """
    ~40% of tasks get 1–3 subtasks.
    """
    for task_id in task_ids:
        if random.random() < 0.4:
            for _ in range(random.randint(1, 3)):
                created_at = random_past_datetime(200)
                completed = random.random() < 0.6

                cursor.execute(
                    "INSERT INTO subtasks VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (
                        str(uuid.uuid4()),
                        task_id,
                        random.choice(user_ids),
                        random.choice(SUBTASK_TEMPLATES),
                        completed,
                        created_at,
                        created_at if completed else None
                    )
                )