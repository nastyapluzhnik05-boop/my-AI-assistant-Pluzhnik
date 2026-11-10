attempts = 0
while True:
    password = input("Введите пароль: ")
    attempts += 1
    if password == "python":
        break

print("Количество попыток:", attempts)
