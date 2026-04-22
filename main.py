import os
from utils import input_non_empty

commands = ("ls", "filter", "search", "size", "stats", "exit", "help")


def ls():
    files = os.listdir()

    if not files:
        print("no files")
        return

    for f in files:
        print(f)


def filter():
    files = os.listdir()

    if not files:
        print("no files")
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
    files = os.listdir()

    if not files:
        print("no files")
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
    pass


def stats():
    pass


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
