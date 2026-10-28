# Journal Application
from pathlib import Path

JOURNAL_FILENAME = "journal.txt"

def read_journal(file_path):
    """Read the journal from a file"""

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            entries = file.readlines()
    except FileNotFoundError:
        return ["Error: The file does not exist!"]

    return [entry.strip() for entry in entries if entry.strip()]

def write_journal(file_path, entry):
    """Write a journal entry to a file"""
    try:
        with open(file_path, 'a', encoding="utf-8") as file:
            file.write(f"{entry}\n")
    except FileNotFoundError:
        print("Cannot write to file, check your file path")

def print_journal(file_path):
    for entry in read_journal(file_path):
        print(entry)

def main():
    file_path = Path(__file__).parent / JOURNAL_FILENAME
    print(file_path)
    while True:
        new_entry = input("Write your new entry (or q to quit):").lower()

        if new_entry == 'q':
            break

        write_journal(file_path, new_entry)

    print_journal(file_path)

if __name__ == "__main__":
    main()