from collections import defaultdict
from datetime import datetime, date
from datetime import timedelta


def get_birthdays_per_week(users: list[dict]):
    """
    >>> user = {"name": "Bill Gates", "birthday": datetime(1955, 12, 5)}
    >>> users = [user]
    >>> get_birthdays_per_week(users)

    :param users:
    :return:
    """
    # Example of output
    # {'Monday': ['Bill Gates'], 'Thursday': ['Jan Koum']}

    # поточна дата
    today = datetime.today().date()
    # знати дати наступного тижня від Понеділка до Неділі
    first_day_of_next_weak = today - timedelta(days=today.weekday()) + timedelta(weeks=1)
    last_day_of_next_weak = first_day_of_this_weak + timedelta(days=6) + timedelta(weeks=1)

    users_that_have_birth_day = defaultdict(list)
    # відфільтрувати наші значення по днях
    for user in users:
        users_birth_day: date = user["birthday"].date()
        users_name = user['name']

        celebration_of_users_birth_day_this_year = users_birth_day.replace(today.year)
        if celebration_of_users_birth_day_this_year < today:
            celebration_of_users_birth_day_this_year = users_birth_day.replace(today.year + 1)

        if first_day_of_next_weak <= celebration_of_users_birth_day_this_year <= last_day_of_next_weak:
            day = celebration_of_users_birth_day_this_year
            users_that_have_birth_day[day].append(users_name)

    sunday = last_day_of_next_weak
    saturday = last_day_of_next_weak - timedelta(days=1)
    for weekday in [saturday, sunday]:
        users_that_hava_birth_day_in_monday = users_that_have_birth_day[first_day_of_next_weak]
        users_that_have_birth_day_in_weekday = users_that_have_birth_day[weekday]
        users_that_hava_birth_day_in_monday.extend(users_that_have_birth_day_in_weekday)
        users_that_have_birth_day.pop(weekday, None)

    if not len(users_that_have_birth_day[first_day_of_next_weak]):
        users_that_have_birth_day.pop(first_day_of_next_weak, None)

    # day: date
    for day in sorted(users_that_have_birth_day.keys()):
        f_str = f'{day.strftime("%A").center(15)} {" ~ ".join(users_that_have_birth_day[day])}'
        print(f_str)


if __name__ == "__main__":
    users = [
        {"name": "u 1", "birthday": datetime(1955, 12, 5)},
        {"name": "u 2", "birthday": datetime(1955, 12, 4)},
        {"name": "u 3", "birthday": datetime(1955, 12, 9)},
        {"name": "u 4", "birthday": datetime(1955, 12, 10)},
        {"name": "u 5", "birthday": datetime(1955, 12, 8)},
    ]
    get_birthdays_per_week(users)
