def get_unique_list_numbers() -> list[int]:
    from random import randint
    unique = []
    while len(unique) != 15:
        for x in range(15):
            x = randint(-10, 10)
        if x in unique:
            continue
        else:
            unique.append(x)
    return unique

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
