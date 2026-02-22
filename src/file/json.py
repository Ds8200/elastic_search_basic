import json


def read_json_file(path: str) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

