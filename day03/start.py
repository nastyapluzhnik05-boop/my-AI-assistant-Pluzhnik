age = int(input("Введите возраст: "))
passs = input("Есть ли у вас пропуск (да/нет): ")
accompaniment = input("Есть ли у вас сопровождение (да/нет): ")
if age >= 18 and passs == "да":
    print("Вы можете войти")
else:
    print("Вы не можете войти")