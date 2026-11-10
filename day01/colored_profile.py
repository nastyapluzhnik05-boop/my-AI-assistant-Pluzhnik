from colorama import Fore, Style

name = input("Введите имя: ")
last_name = input("Введите фамилию: ")
group = input("Введите вашу группу: ")
print(Fore.GREEN + "===КАРТОЧКА===")
print(Fore.CYAN + f"Имя: {name}")
print(Fore.CYAN + f"Фамилия: {last_name}")
print(Fore.CYAN + f"Группа: {group}")
print(Style.RESET_ALL)