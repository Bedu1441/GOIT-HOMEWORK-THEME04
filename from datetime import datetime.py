from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Обчислює кількість днів між заданою датою і поточною.
    Повертає додатне число, якщо дата в минулому,
    та від’ємне — якщо дата в майбутньому.
    """

    try:
        # Перетворення рядка у дату
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Невірний формат дати. Використовуйте 'YYYY-MM-DD'.")

    # Поточна дата (без часу)
    today = datetime.today().date()

    # Різниця у днях (може бути від’ємною)
    delta = today - target_date

    return delta.days
