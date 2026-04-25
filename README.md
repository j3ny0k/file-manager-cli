# File Manager CLI

Simple CLI tool for working with files in the current directory.

The app can list files, search by name, filter by extension, show file sizes, and display basic file statistics.

---

## Features

- list files and folders in the current directory
- search files by name
- filter files by extension
- show file sizes
- show total number of files
- show total size of files
- case-insensitive search
- extension filter supports input with or without dot
- empty input handling
- invalid command handling

---

## Usage

Run the program:

```bash
python main.py
```

Available commands:

```text
ls / search / filter / size / stats / help / exit
```

---

## Commands

### ls

Show all items in the current directory.

Example:

```text
command: ls
main.py
utils.py
README.md
notes.txt
```

---

### search

Search files and folders by name.

The search is case-insensitive.

Example:

```text
command: search

search: main
main.py
```

If nothing is found:

```text
not found
```

---

### filter

Filter files and folders by extension.

You can enter the extension with or without a dot.

Example:

```text
command: filter

ext: py
main.py
utils.py
```

This works the same as:

```text
ext: .py
```

If nothing is found:

```text
not found
```

---

### size

Show size for files in the current directory.

Folders are skipped.

Example:

```text
command: size
main.py – 2.10 KB
utils.py – 120 B
README.md – 1.50 KB
```

---

### stats

Show basic file statistics.

Folders are skipped.

Example:

```text
command: stats
files: 3
total size: 3.72 KB
```

---

### help

Show available commands.

Example:

```text
command: help
allowed commands: ls, filter, search, size, stats, exit, help
```

---

### exit

Exit the program.

---

## Project structure

```text
main.py   # main CLI logic
utils.py  # shared input helper
```

---

## Notes

- the app works in the current directory
- `ls`, `search`, and `filter` use all items from the current directory
- `size` and `stats` only process files
- file sizes are formatted as B, KB, or MB
- search is case-insensitive
- filter is case-insensitive
- empty input is handled
- invalid command is handled

---

## Status

Finished learning project.

This project practices:

- working with the file system using `os`
- CLI architecture
- command handling
- file filtering
- file size calculation
- basic input validation
