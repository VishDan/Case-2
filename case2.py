import datetime

def get_user_birthday():
    day = int(input("Введите день рождения: "))
    month = int(input("Введите месяц рождения: "))
    year = int(input("Введите год рождения: "))
    return datetime.date(year, month, day)

def get_day_of_week(date):
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[date.weekday()]

def is_leap_year(year):
    return year % 4 == 0 and (year % 100!= 0 or year % 400 == 0)

def get_user_age(birthday):
    today = datetime.date.today()
    age = today.year - birthday.year
    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1
    return age

def print_birthday(date):
    day_str = str(date.day).zfill(2)
    month_str = str(date.month).zfill(2)
    year_str = str(date.year).zfill(4)
    print(f"{day_str[0]}*{day_str[1]} {month_str[0]}*{month_str[1]} {year_str[0]}*{year_str[1]}*{year_str[2]}*{year_str[3]}")

def main():
    birthday = get_user_birthday()
    print("День недели рождения:", get_day_of_week(birthday))
    print("Високосный год:", "Да" if is_leap_year(birthday.year) else "Нет")
    print("Возраст:", get_user_age(birthday))
    print("Дата рождения:")
    print_birthday(birthday)

if __name__ == "__main__":
    main()
    