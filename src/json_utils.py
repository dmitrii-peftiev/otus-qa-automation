import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def read_json(filename: str) -> list:
    file_path = BASE_DIR / "data" / filename
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    users_list = []
    for user in data:
        users_list.append(
            {
                "name": user.get("name"),
                "gender": user.get("gender"),
                "address": user.get("address"),
                "age": user.get("age"),
                "books": [],
            }
        )
    return users_list


def read_csv(filename: str) -> list:
    file_path = BASE_DIR / "data" / filename
    books_list = []
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            pages_value = row.get("Pages")
            books_list.append(
                {
                    "title": row.get("Title"),
                    "author": row.get("Author"),
                    "pages": int(pages_value) if pages_value else 0,
                    "genre": row.get("Genre"),
                }
            )
    return books_list


def write_json(filename: str, data: list) -> None:
    file_path = BASE_DIR / "data" / filename
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    users = read_json("users.json")
    books = read_csv("books.csv")

    print(f"Loaded {len(users)} users from JSON")
    print(f"Loaded {len(books)} books from CSV")

    for i, book in enumerate(books):
        user_index = i % len(users)
        users[user_index]["books"].append(book)

    write_json("result.json", users)
    print("Result successfully saved to result.json")
