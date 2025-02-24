import random

def fill_list_different():
    """Создает пустой список и заполняет его случайными числами по одному, но только нечетными."""
    lst = []
    for _ in range(10):
        lst.append(random.randint(1, 50) * 2 - 1)
    return lst
