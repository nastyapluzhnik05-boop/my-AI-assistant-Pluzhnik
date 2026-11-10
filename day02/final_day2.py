project_name = input("Введите название проекта: ")
participants = int(input("Введите количество участников: "))
resource_cost = float(input("Введите стоимость ресурса на одного участника за месяц: "))
months = int(input("Введите количество месяцев работы: "))
responsible = input("Введите имя ответственного студента: ")

monthly_expense = participants * resource_cost
total_expense = monthly_expense * months
project_name_length = len(project_name)

print("=" * 40)
print(" " * 6 + "РАСЧЁТ РАСХОДОВ IT-ПРОЕКТА")
print("=" * 40)

print("Название проекта: " + project_name)
print("Ответственный студент: " + responsible)
print("Количество участников:", participants)
print("Расход за один месяц:", monthly_expense)
print("Общий расход за", months, "мес.:", total_expense)
print("Количество символов в названии:", project_name_length)
print("Первый символ названия:", project_name[0])
print("Последний символ названия:", project_name[-1])

print("=" * 40)
