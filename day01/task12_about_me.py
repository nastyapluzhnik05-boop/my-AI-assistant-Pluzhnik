from colorama import Fore, Style

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
age = input("Введите возраст: ")
group = input("Введите группу: ")
speciality = input("Введите специальность: ")
subject = input("Введите любимый школьный предмет: ")
interest = input("Какая область IT вас интересует? ")
hobby = input("Какое у вас хобби? ")

print(Fore.CYAN + "=== МОЙ ПРОФИЛЬ ===")
print(Style.RESET_ALL)

print("Имя:", name)
print("Фамилия:", surname)
print("Возраст:", age)
print("Группа:", group)
print("Специальность:", speciality)
print("Любимый предмет:", subject)
print("Интересующая область IT:", interest)
print("Хобби:", hobby)

print(Fore.GREEN + "Профиль создан")
print(Style.RESET_ALL)