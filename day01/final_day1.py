from colorama import Fore, Style

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
group = input("Введите группу: ")
speciality = input("Введите специальность: ")
interest = input("Введите интересующую область IT: ")

age = input("Введите возраст: ")
hobby = input("Введите хобби: ")
goal = input("Какова ваша цель в обучении? ")

print(Fore.CYAN + "===================================")
print("       КАРТОЧКА СТУДЕНТА")
print("===================================")
print(Style.RESET_ALL)

print("Имя:", name, surname)
print("Группа:", group)
print("Специальность:", speciality)
print("Интересующая область IT:", interest)
print("Возраст:", age)
print("Хобби:", hobby)
print("Цель обучения:", goal)

print(Fore.GREEN + "\nРабочее окружение подготовлено")
print(Style.RESET_ALL)

print("Работа завершена")