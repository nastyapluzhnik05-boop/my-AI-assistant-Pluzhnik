from colorama import Fore, Style

name = input("Введите имя: ")
last_name = input("Введите фамилию: ")
group = input("Введите вашу группу: ")
progect = input("Введите название проекта: ")
role = input("Какая ваша роль в этом проекте? ")
tecnology = input("Какую технологию вы бы хотели изучить? ")

print(Fore.GREEN + "========================================")
print(Fore.RED + "              ВАША КАРТОЧКА")
print(Fore.GREEN + "========================================")

print(Fore.BLUE + "Имя: " + name)
print(Fore.BLUE + "Фамилия: " + last_name)
print(Fore.BLUE + "Группа: " + group)
print(Fore.BLUE + "Проект: " + progect)
print(Fore.BLUE + "Роль: " + role)
print(Fore.BLUE + "Изучение технологии: " + tecnology)
