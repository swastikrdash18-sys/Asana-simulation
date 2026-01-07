from db import get_connection, run_schema
from generators.organizations import generate_organization
from generators.teams import generate_teams
from generators.users import generate_users
from generators.team_memberships import generate_team_memberships
from generators.projects import generate_projects
from generators.sections import generate_sections
from generators.tasks import generate_tasks
from generators.subtasks import generate_subtasks
from generators.comments import generate_comments
from generators.tags import generate_tags, assign_tags
from generators.custom_fields import generate_custom_fields

def main():
    run_schema()
    conn = get_connection()
    cur = conn.cursor()

    org_id = generate_organization(cur)
    team_ids = generate_teams(cur, org_id)
    user_ids = generate_users(cur, org_id, n=200)   # scale later
    generate_team_memberships(cur, team_ids, user_ids)

    project_ids = generate_projects(cur, org_id, team_ids)
    section_map = generate_sections(cur, project_ids)

    task_ids = generate_tasks(cur, project_ids, section_map, user_ids)
    generate_subtasks(cur, task_ids, user_ids)
    generate_comments(cur, task_ids, user_ids)

    tag_ids = generate_tags(cur)
    assign_tags(cur, task_ids, tag_ids)

    generate_custom_fields(cur, project_ids, task_ids)

    conn.commit()
    conn.close()
    print("FULL ASANA-STYLE DATASET CREATED SUCCESSFULLY")

if __name__ == "__main__":
    main()
