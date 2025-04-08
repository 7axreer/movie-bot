# utils/database.py

import json
import os
from config import FILE_NAME

def load_database():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_to_json(code, title, quality, audio, subtitle, file_id):
    data = load_database()
    data[str(code)] = {
        "title": title,
        "quality": quality,
        "audio": audio,
        "subtitle": subtitle,
        "file_id": file_id
    }
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def delete_movie(code):
    data = load_database()
    if code in data:
        del data[code]
        with open(FILE_NAME, "w") as f:
            json.dump(data, f, indent=4)
        return True
    return False
def get_all_users():
    with open("database.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return list(data.get("users", {}).keys())
