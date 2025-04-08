import json
import os

USER_DB_PATH = "database.json"

def get_all_users():
    if not os.path.exists(USER_DB_PATH):
        return []

    with open(USER_DB_PATH, "r") as f:
        data = json.load(f)

    return list(data.get("users", {}).keys())
