import uuid
import random

FIELDS = [
    ("Priority", ["High", "Medium", "Low"]),
    ("Effort", ["1", "2", "3", "5", "8"])
]

def generate_custom_fields(cursor, project_ids, task_ids):
    for project_id in project_ids:
        for name, values in FIELDS:
            field_id = str(uuid.uuid4())
            cursor.execute(
                "INSERT INTO custom_field_definitions VALUES (?, ?, ?, ?)",
                (field_id, project_id, name, "enum")
            )

            for task_id in random.sample(task_ids, min(10, len(task_ids))):
                cursor.execute(
                    "INSERT INTO custom_field_values VALUES (?, ?, ?, ?)",
                    (
                        str(uuid.uuid4()),
                        field_id,
                        task_id,
                        random.choice(values)
                    )
                )