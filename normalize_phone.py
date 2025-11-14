import re

def normalize_phone(phone_number):
    """
    Нормалізує телефонний номер до формату:
    - лише '+' (на початку) та цифри
    - якщо міжнародний код відсутній — додається '+38'
    - якщо номер починається з '380' — додається '+' і номер лишається
    """

    # Видаляємо всі символи, крім цифр та '+'
    cleaned = re.sub(r"[^\d+]", "", phone_number)

    # Якщо починається з '+380' — вже нормальний випадок
    if cleaned.startswith("+380"):
        return cleaned

    # Якщо починається з '380' — треба додати тільки '+'
    if cleaned.startswith("380"):
        return "+" + cleaned

    # Якщо починається з '0' — додаємо +38 (отримується +380…)
    if cleaned.startswith("0"):
        return "+38" + cleaned

    # Якщо номер без коду, але починається з будь-яких цифр — теж додаємо +38
    if cleaned and cleaned[0].isdigit() and not cleaned.startswith("+"):
        return "+38" + cleaned

    # Якщо номер вже починається з '+' але з іншим кодом — залишаємо як є
    return cleaned
