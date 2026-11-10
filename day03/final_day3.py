name = input("Введите имя участника: ")
age = int(input("Введите возраст: "))

if age < 16:
    print("Возраст не подходит")
else:
    course = input("Введите курс: ")
    agreement = input("Есть ли у вас согласие на участие (да/нет): ")
    if age >= 16 and agreement != "да":
            print("Нет согласия на участие")
    elif age >= 16 and agreement == "да":
        ball = int(input("Введите набранный вами балл от 0 до 100: "))
        if ball >= 90 and ball <= 100:
                print("Высокий результат")
        elif ball >= 70 and ball < 90:
                print("Хороший результат")
        elif ball >= 50 and ball < 70:
                print("Допустимый результат")
        else:
            if ball < 50 and ball > 0:
                print("Результат недостаточен")
            elif ball > 100 or ball < 0:
                print("Некорректный балл")
              
if age >= 16 and agreement == "да" and ball >= 50 and ball <= 100:
    print(f"Участник: {name}, возраст: {age}, курс: {course}, прошел с баллом: {ball}")