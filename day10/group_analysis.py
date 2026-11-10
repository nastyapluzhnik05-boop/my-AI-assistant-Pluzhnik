import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Группа": ["А", "А", "А", "А", "А", "Б", "Б", "Б", "Б", "Б"],
    "Имя": ["Анна", "Иван", "Олег", "Маша", "Пётр", "Ева", "Дима", "Лена", "Саша", "Коля"],
    "Баллы": [80, 65, 90, 70, 55, 60, 85, 75, 95, 50],
    "Посещаемость": [90, 80, 100, 85, 70, 75, 95, 90, 100, 65]
}

df = pd.DataFrame(data)
df.to_csv("students.csv", index=False, encoding="utf-8-sig")
print(df)

