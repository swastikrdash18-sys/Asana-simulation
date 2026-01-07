import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "output", "asana_simulation.sqlite")
SCHEMA_PATH = os.path.join(BASE_DIR, "schema.sql")

def get_connection():
    os.makedirs(os.path.join(BASE_DIR, "output"), exist_ok=True)
    return sqlite3.connect(DB_PATH)

def run_schema():
    conn = get_connection()
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()