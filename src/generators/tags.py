import uuid
import random

TAGS = ["urgent", "backend", "frontend", "customer-request", "tech-debt"]

def generate_tags(cursor):
    tag_ids = []
    for tag in TAGS:
        tag_id = str(uuid.uuid4())
        cursor.execute("INSERT INTO tags VALUES (?, ?)", (tag_id, tag))
        tag_ids.append(tag_id)
    return tag_ids

def assign_tags(cursor, task_ids, tag_ids):
    for task_id in random.sample(task_ids, int(len(task_ids) * 0.4)):
        for tag_id in random.sample(tag_ids, random.randint(1, 2)):
            cursor.execute(
                "INSERT OR IGNORE INTO task_tags VALUES (?, ?)",
                (task_id, tag_id)
            )