# File CLI

CLI-инструмент для работы с файлами в текущей папке.

---

## Возможности

- ls — показать все файлы
- search — поиск по имени файла
- filter — фильтр по расширению
- size — показать размер файлов
- stats — общая информация (кол-во и размер)

---

## Примеры

```text
command: ls
→ main.py
→ notes.txt
```

```text
command: search
search: main
→ main.py
```

```text
command: filter
ext: .py
→ main.py
```

```text
command: size
→ main.py – 1200 bytes
→ notes.txt – 300 bytes
```

```text
command: stats
→ files: 5
→ total size: 2300 bytes
```

---

## Запуск

```bash
python main.py
```

---

## Команды

```
ls / search / filter / size / stats / help / exit
```

---

## Особенности

- работает в текущей директории
- поиск без учёта регистра
- filter поддерживает ввод без точки (py → .py)
- есть базовая обработка ошибок

---

## Структура

- main.py — логика CLI
- utils.py — ввод

---

## Цель проекта

Практика:

- работы с файловой системой (os)
- обработки данных
- CLI-архитектуры
