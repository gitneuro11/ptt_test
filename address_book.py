#!/usr/bin/env python3
"""Simple command-line address book application."""

# 주소록을 JSON 파일로 관리하는 간단한 CLI 애플리케이션입니다.
import json
from pathlib import Path

DATA_FILE = Path("address_book.json")


def load_entries():
    # 저장된 주소록 JSON 파일을 읽어 리스트로 역직렬화한다.
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except json.JSONDecodeError:
        return []


def save_entries(entries):
    # 현재 메모리상의 주소록 데이터를 JSON 파일로 저장한다.
    with DATA_FILE.open("w", encoding="utf-8") as handle:
        json.dump(entries, handle, ensure_ascii=False, indent=2)


def prompt_entry():
    # 사용자에게 항목 정보를 입력받아 딕셔너리로 구성한다.
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    return {"name": name, "phone": phone, "email": email}


def list_entries(entries):
    # 저장된 모든 주소록 항목을 번호와 함께 출력한다.
    if not entries:
        print("No entries found.")
        return
    for index, entry in enumerate(entries, start=1):
        print(f"{index}. {entry['name']} | {entry['phone']} | {entry['email']}")


def delete_entry(entries):
    # 사용자가 선택한 번호에 해당하는 항목을 삭제한다.
    if not entries:
        print("No entries to delete.")
        return
    list_entries(entries)
    selection = input("Enter the number of the entry to delete (or press Enter to cancel): ").strip()
    if not selection:
        print("Deletion cancelled.")
        return
    if not selection.isdigit():
        print("Invalid selection.")
        return
    index = int(selection)
    if not 1 <= index <= len(entries):
        print("Selection out of range.")
        return
    removed = entries.pop(index - 1)
    save_entries(entries)
    print(f"Deleted entry for {removed['name']}.")


def main():
    # 메뉴를 보여주고 사용자의 선택을 처리하는 메인 루프를 실행한다.
    entries = load_entries()
    actions = {
        "1": "Add entry",
        "2": "List entries",
        "3": "Delete entry",
        "4": "Exit",
    }
    while True:
        print("Address Book")
        for key, label in actions.items():
            print(f"{key}. {label}")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            entry = prompt_entry()
            entries.append(entry)
            save_entries(entries)
            print("Entry saved.")
        elif choice == "2":
            list_entries(entries)
        elif choice == "3":
            delete_entry(entries)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
