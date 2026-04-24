import os
from utils import input_non_empty

commands = ("ls", "filter", "search", "size", "stats", "exit", "help")


def get_files():
    files = os.listdir()

    if not files:
        print("no files")
        return

    return files


def ls():
    files = get_files()

    if not files:
        return

    for name in files:
        print(name)


def filter():
    files = get_files()

    if not files:
        return

    ext = input_non_empty("\next: ").lower()

    if not ext.startswith("."):
        ext = "." + ext

    found = False

    for name in files:
        if name.lower().endswith(ext):
            print(name)
            found = True

    if not found:
        print("not found")


def search():
    files = get_files()

    if not files:
        return

    query = input_non_empty("\nsearch: ").lower()

    found = False

    for name in files:
        if query in name.lower():
            print(name)
            found = True

    if not found:
        print("not found")


def size():
    files = get_files()

    if not files:
        return

    for name in files:
        if os.path.isfile(name):
            size = os.path.getsize(name)
            print(f"{name} – {size} bytes")


def stats():
    files = get_files()

    if not files:
        return

    total = 0
    result = 0

    for name in files:
        if os.path.isfile(name):
            size = os.path.getsize(name)
            total += size
            result += 1

    print(f"files: {result}")
    print(f"total size: {total} bytes")


def main():
    print("type help to show commands")

    while True:
        command = input_non_empty("\ncommand: ").lower()

        if command == "help":
            print("allowed commands:", ", ".join(commands))

        elif command not in commands:
            print("invalid command:", command)
            print("available:", ", ".join(commands))

        elif command == "exit":
            break

        elif command == "ls":
            ls()

        elif command == "filter":
            filter()

        elif command == "search":
            search()

        elif command == "size":
            size()

        elif command == "stats":
            stats()


if __name__ == "__main__":
    main()
