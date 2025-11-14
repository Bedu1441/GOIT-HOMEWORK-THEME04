from datetime import datetime, date, timedelta


def get_upcoming_birthdays(users):
    """
    Повертає список колег, яких треба привітати протягом
    наступних 7 днів (включно з сьогодні).
    
    Якщо день народження припадає на вихідний (субота/неділя),
    дата привітання переноситься на наступний понеділок.
    
    Формат результату:
    [
        {"name": <ім'я>, "congratulation_date": "YYYY.MM.DD"},
        ...
    ]
    """
    
    today = date.today()
    upcoming = []

    for user in users:
        # 1. Парсимо дату народження
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # 2. День народження у поточному році
        birthday_this_year = birthday.replace(year=today.year)

        # 3. Якщо вже минув у цьому році — беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # 4. Різниця у днях між сьогодні і ДН
        delta_days = (birthday_this_year - today).days

        # 5. Цікавлять дні від 0 до 7 включно
        if 0 <= delta_days <= 7:
            congrat_date = birthday_this_year

            # 6. Якщо це вихідний — переносимо на понеділок
            # weekday(): 0=понеділок, ..., 5=субота, 6=неділя
            if congrat_date.weekday() == 5:      # субота
                congrat_date += timedelta(days=2)
            elif congrat_date.weekday() == 6:    # неділя
                congrat_date += timedelta(days=1)

            # 7. Додаємо до результату
            upcoming.append({
                "name": user["name"],
                "congratulation_date": congrat_date.strftime("%Y.%m.%d")
            })

    # (опційно) сортуємо за датою привітання
    upcoming.sort(key=lambda x: x["congratulation_date"])
    return upcoming
