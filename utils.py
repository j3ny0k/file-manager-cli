def input_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("input is empty")
