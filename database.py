import json
import os
from typing import Dict, Any

DATABASE_PATH = "database.json"


def load_data() -> Dict[str, Any]:
    if not os.path.exists(DATABASE_PATH):
        return {}
    with open(DATABASE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data: Dict[str, Any]):
    with open(DATABASE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def save_movie(code: str, title: str, quality: str, audio: str, subtitle: str, file_id: str):
    data = load_data()
    data[code] = {
        "title": title,
        "quality": quality,
        "audio": audio,
        "subtitle": subtitle,
        "file_id": file_id
    }
    save_data(data)


def get_movie_by_code(code: str) -> Dict[str, Any] | None:
    data = load_data()
    return data.get(code)


def save_user(user_id: int):
    data = load_data()
    if "users" not in data:
        data["users"] = []
    if user_id not in data["users"]:
        data["users"].append(user_id)
        save_data(data)


def get_all_user_ids():
    data = load_data()
    return data.get("users", [])
