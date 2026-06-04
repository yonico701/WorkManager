import json
import os


def save_to_json(file_path, data):
    project_root = os.path.dirname(os.path.dirname(__file__))
    full_path = os.path.join(project_root, file_path)

    folder_path = os.path.dirname(full_path)
    os.makedirs(folder_path, exist_ok=True)

    with open(full_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_from_json(file_path):
    project_root = os.path.dirname(os.path.dirname(__file__))
    full_path = os.path.join(project_root, file_path)

    if not os.path.exists(full_path):
        return []

    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data






