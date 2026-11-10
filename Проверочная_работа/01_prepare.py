A = 17 % 5
B = 17 % 4
T = 65 + A
P = 75 + B

name = input("Введите вашу фамилию: ")
age = int(input("Введите ваш номер: "))
while age < 1 or age > 30:
    age = int(input("Введите ваш номер еще раз: "))

from colorama import Fore, Style
print(Fore.GREEN + "=" * 30)
print(Fore.YELLOW + "Ваша фамилия: " + Fore.CYAN + name)
print(Fore.YELLOW + "Ваш номер: " + Fore.CYAN + str(age))
print(Fore.YELLOW + "A =", A, "B =", B, "T =", 65 + A, "P =", 75 + B)
print(Fore.GREEN + "=" * 30 + Style.RESET_ALL)

students = [
    {
        "ID": 1,
        "Имя": "Анна",
        "Группа": "Альфа",
        "Тест1": 54,
        "Тест2": 62,
        "Тест3": 70,
        "Посещаемость": 71
    },
    {
        "ID": 2,
        "Имя": "Борис",
        "Группа": "Бета",
        "Тест1": 76,
        "Тест2": 80,
        "Тест3": 84,
        "Посещаемость": 82
    },
    {
        "ID": 3,
        "Имя": "Вера",
        "Группа": "Гамма",
        "Тест1": 88,
        "Тест2": 92,
        "Тест3": 86,
        "Посещаемость": 90
    },
    {
        "ID": 4,
        "Имя": "Глеб",
        "Группа": "Альфа",
        "Тест1": 60,
        "Тест2": "", 
        "Тест3": 68,
        "Посещаемость": 76
    },
    {
        "ID": 5,
        "Имя": "Дарья",
        "Группа": "Бета",
        "Тест1": 70,
        "Тест2": 74,
        "Тест3": 78,
        "Посещаемость": 79
    },
    {
        "ID": 6,
        "Имя": "Егор",
        "Группа": "Гамма",
        "Тест1": 40,
        "Тест2": 55,
        "Тест3": 50,
        "Посещаемость": 68
    },
    {
        "ID": 7,
        "Имя": "Жанна",
        "Группа": "Альфа",
        "Тест1": 80,
        "Тест2": 84,
        "Тест3": 88,
        "Посещаемость": 92
    },
    {
        "ID": 8,
        "Имя": "Захар",
        "Группа": "Бета",
        "Тест1": 58,
        "Тест2": 64,
        "Тест3": 60,
        "Посещаемость": 74
    },
    {
        "ID": 9,
        "Имя": "Ирина",
        "Группа": "Гамма",
        "Тест1": 90,
        "Тест2": 94,
        "Тест3": 92,
        "Посещаемость": 95
    },
    {
        "ID": 10,
        "Имя": "Кирилл",
        "Группа": "Альфа",
        "Тест1": 66,
        "Тест2": 70,
        "Тест3": 72,
        "Посещаемость": 80
    },
    {
        "ID": 11,
        "Имя": "Лена",
        "Группа": "Бета",
        "Тест1": 72,
        "Тест2": "", 
        "Тест3": 76,
        "Посещаемость": 77
    },
    {
        "ID": 12,
        "Имя": "Максим",
        "Группа": "Гамма",
        "Тест1": 48,
        "Тест2": 52,
        "Тест3": 56,
        "Посещаемость": 72
    }
]

add_test = 2
add_attend = 1
for student in students:
    if student["Тест2"] != "":
        student["Тест2"] += 2
    student["Тест1"] += 2
    student["Тест3"] += 2
    student["Посещаемость"] += 1

print(students[0])
print(students[-1])
print(students[1]["Группа"])
print(len(students))
groups = ["Альфа", "Бета", "Гамма"]
# user_group = input("Введите название группы: ")
# if user_group in groups:
#     print("Группа есть в списке")
# else:
#     print("Группы нет в списке")

students_2 = ["Михаил", "Надежда", "Анна", "Антон", "Олег", "Никита"]
students_2.append("Максим")
print(len(students_2))
students_2.pop()
print(len(students_2))

for i in range(len(students)):
    if students[i]["Тест2"] == "":
        print(i, "индекс, где пропущено число")

total_scores = 0
count_scores = 0
dopusk_count = 0


for student in students:
    student["Пропуск_Тест2"] = student["Тест2"] == ""

    if student["Тест2"] == "":
        student["Тест2"] = 0

    total = student["Тест1"] + student["Тест2"] + student["Тест3"]
    average = total / 3
  
    if average >= 85:
        student["Уровень"] = "высокий уровень"
    elif average >= T:
        student["Уровень"] = "базовый уровень"
    else:
        student["Уровень"] = "требуется подготовка"
    
    if average >= T and student["Посещаемость"] >= P and student["Пропуск_Тест2"] == False:
        student["Допуск"] = "допуск"
        dopusk_count += 1
    else:
        student["Допуск"] = "недопуск"

    student["Сумма"] = total
    total_scores += total
    count_scores += 3
    
    student["Среднее"] = average
    

    student["Причины недопуска"] = []
    if student["Среднее"] < T:
        student["Причины недопуска"].append("низкое среднее")
    if student["Посещаемость"] < P:
        student["Причины недопуска"].append("низкая посещаемость")
    if student["Пропуск_Тест2"] == True:
        student["Причины недопуска"].append("отсуствие тестового результата")

overall_average = total_scores / count_scores
print(overall_average)

with open("source.csv", "w", encoding="utf-8") as file:
    file.write("ID,Имя,Группа,Тест1,Тест2,Тест3,Посещаемость\n")

    for student in students:
        if student["Пропуск_Тест2"]:
            test2 = ""
        else:
            test2 = student["Тест2"]

        file.write(
            f'{student["ID"]},{student["Имя"]},{student["Группа"]},'
            f'{student["Тест1"]},{test2},{student["Тест3"]},'
            f'{student["Посещаемость"]}\n'
        )

executor = input("Введите фамилию исполнителя: ")
N = 17

with open("results_python_report.txt", "w", encoding="utf-8") as file:
    file.write(f"Исполнитель: {executor}\n")
    file.write(f"Вариант: {N}\n")
    file.write(f"A = {A}, B = {B}, T = {T}, P = {P}\n\n")

    file.write("Результаты участников:\n")

    for student in students:
        reasons = student["Причины недопуска"]

        if len(reasons) == 0:
            reasons_text = "нет"
        else:
            reasons_text = ""
            for reason in reasons:
                if reasons_text == "":
                    reasons_text = reason
                else:
                    reasons_text += ", " + reason

        file.write(
            f'ID: {student["ID"]}; '
            f'Среднее: {student["Среднее"]:.2f}; '
            f'Уровень: {student["Уровень"]}; '
            f'Допуск: {student["Допуск"]}; '
            f'Причины: {reasons_text}\n'
        )

    file.write("\nОбщие показатели:\n")
    file.write(f"Общая сумма баллов: {total_scores}\n")
    file.write(f"Среднее всех результатов: {overall_average:.2f}\n")
    file.write(f"Количество допущенных: {dopusk_count}\n")

    file.write("\nПроверки условий допуска:\n")
    file.write("Среднее T, посещаемость P, все тесты есть: допуск\n")
    file.write("Среднее T - 0.01 при остальных тех же условиях: недопуск\n")
    file.write("Среднее T, посещаемость P - 1: недопуск\n")
    file.write("Среднее T, посещаемость P, Тест2 пропущен: недопуск\n")

with open("source.csv", "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines[:3]:
    print(line)

count_rows = 0

for line in lines[1:]:
    count_rows += 1

print("Количество строк данных:", count_rows)

with open("journal.txt", "a", encoding="utf-8") as file:
    file.write("Этап 3 завершён. Вариант: 17\n")
