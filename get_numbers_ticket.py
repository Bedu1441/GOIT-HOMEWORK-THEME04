import random

def get_numbers_ticket(min_value, max_value, quantity):
    """
    Генерує відсортований список унікальних випадкових чисел у заданому діапазоні.
    
    Параметри:
        min_value (int): мінімальне число (не менше 1)
        max_value (int): максимальне число (не більше 1000)
        quantity (int): кількість чисел для вибору
        
    Повертає:
        list: відсортований список унікальних випадкових чисел
              або пустий список, якщо параметри некоректні.
    """

    # Перевірка валідності параметрів
    if (
        not isinstance(min_value, int) or
        not isinstance(max_value, int) or
        not isinstance(quantity, int) or
        min_value < 1 or
        max_value > 1000 or
        min_value > max_value or
        quantity <= 0 or
        quantity > (max_value - min_value + 1)
    ):
        return []

    # Генерація унікальних чисел
    numbers = random.sample(range(min_value, max_value + 1), quantity)

    # Повертаємо відсортований список
    return sorted(numbers)
