import uuid

SECTION_TEMPLATES = [
    "Backlog",
    "To Do",
    "In Progress",
    "Review",
    "Done"
]

def generate_sections(cursor, project_ids):
    """
    Each project gets the same standard workflow sections.
    """
    section_map = {}

    for project_id in project_ids:
        section_map[project_id] = []
        for position, name in enumerate(SECTION_TEMPLATES):
            section_id = str(uuid.uuid4())
            cursor.execute(
                "INSERT INTO sections VALUES (?, ?, ?, ?)",
                (section_id, project_id, name, position)
            )
            section_map[project_id].append(section_id)

    return section_map