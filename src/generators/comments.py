import uuid
import random
from utils.dates import random_past_datetime

COMMENTS = [
    "Blocked due to dependency.",
    "PR merged, pending deploy.",
    "Waiting for design feedback.",
    "Resolved and verified.",
    "Need clarification from stakeholder."
]

def generate_comments(cursor, task_ids, user_ids):
    for task_id in random.sample(task_ids, int(len(task_ids) * 0.3)):
        for _ in range(random.randint(1, 3)):
            cursor.execute(
                "INSERT INTO comments VALUES (?, ?, ?, ?, ?)",
                (
                    str(uuid.uuid4()),
                    task_id,
                    random.choice(user_ids),
                    random.choice(COMMENTS),
                    random_past_datetime(180)
                )
            )