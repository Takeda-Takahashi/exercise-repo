import random

def generate_list_different():
    """Создает и возвращает список из 10 случайных четных чисел от 2 до 100"""
    return [random.randint(1, 50) * 2 for _ in range(10)]
