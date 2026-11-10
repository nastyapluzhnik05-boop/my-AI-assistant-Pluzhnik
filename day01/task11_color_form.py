from colorama import Fore, Style

name = input("Введите имя: ")
last_name = input("Введите фамилию: ")
group = input("Введите вашу группу: ")
specialty = input("Введите вашу специальность: ")

print(Fore.GREEN + "========================================")
print(Fore.RED + "       РЕЗУЛЬТАТ ПРАКТИЧЕСКОЙ РАБОТЫ")
print(Fore.GREEN + "========================================")
print(Fore.CYAN + f"Имя: {name}")
print(Fore.CYAN + f"Фамилия: {last_name}")
print(Fore.CYAN + f"Группа: {group}")
print(Fore.CYAN + f"Специальность: {specialty}")
print("")
print(Fore.GREEN + "Работа завершена")
print(Style.RESET_ALL)