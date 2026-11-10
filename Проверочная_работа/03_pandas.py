import pandas as pd

df = pd.read_csv("source.csv")

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())


df["Пропуск_Тест2"] = df["Тест2"].isna()
print(df.isna().sum())
print(df.loc[df["Пропуск_Тест2"], ["ID", "Имя", "Тест2"]])


df_drop = df.copy()
df_drop = df_drop.dropna()
print(df_drop["ID"].tolist())
df["Тест2"] = df["Тест2"].fillna(0)
print(df.isna().sum())
print(df[["ID", "Имя", "Тест2", "Пропуск_Тест2"]])


T = 67
P = 76

df["Сумма"] = df["Тест1"] + df["Тест2"] + df["Тест3"]
df["Среднее"] = df["Сумма"] / 3
levels = []

for average in df["Среднее"]:
    if average >= 85:
        levels.append("высокий")
    elif average >= T:
        levels.append("базовый")
    else:
        levels.append("требуется подготовка")

df["Уровень"] = levels

df["Допуск"] = ((df["Среднее"] >= T) & (df["Посещаемость"] >= P) & (df["Тест2"] != 0))
print(df[["ID", "Сумма", "Среднее", "Уровень", "Допуск"]])


df["Среднее_округл"] = df["Среднее"].round(2)
print(df[["ID", "Среднее", "Среднее_округл"]])

averages = pd.Series(df["Среднее"].values, index=df["ID"])
print(averages.loc[4])

df_indexed = df.copy()
df_indexed = df_indexed.set_index("ID")
print(df_indexed.loc[4])
print(df_indexed.iloc[3])

df.to_csv("results_cleaned.csv", index=False, encoding="utf-8")

cleaned = pd.read_csv("results_cleaned.csv")
print(cleaned.shape)
print(cleaned["ID"].tolist())
print(cleaned.isna().sum())
print(cleaned["Пропуск_Тест2"].sum())

import numpy as np

print(df[["Тест1", "Тест2", "Тест3"]].to_numpy().sum())
print(df[["Тест1", "Тест2", "Тест3"]].to_numpy().mean())
print(df["Допуск"].sum())

admitted = df.loc[df["Допуск"]].copy()
admitted = admitted.sort_values(
    by=["Среднее", "ID"],
    ascending=[False, True]
)
admitted = admitted[
    ["ID", "Имя", "Группа", "Среднее", "Посещаемость"]
]
print(admitted)
admitted.to_csv("admitted.csv", index=False, encoding="utf-8")

attention = df.copy()

attention["Низкое_среднее"] = attention["Среднее"] < T
attention["Низкая_посещаемость"] = attention["Посещаемость"] < P
attention["Пропуск_результата"] = attention["Тест2"] == 0
attention = attention.loc[(attention["Низкое_среднее"]) | (attention["Низкая_посещаемость"]) | (attention["Пропуск_результата"])]
attention = attention[["ID", "Имя", "Группа", "Среднее", "Посещаемость", "Низкое_среднее", "Низкая_посещаемость", "Пропуск_результата"]]
print(attention)
attention.to_csv("attention.csv", index=False, encoding="utf-8")

strong_attendance = df.loc[(df["Среднее"] >= T) & (df["Посещаемость"] >= P)].copy()

strong_attendance = strong_attendance[["ID", "Имя", "Группа", "Среднее", "Посещаемость"]]
print(strong_attendance)
strong_attendance.to_csv("strong_attendance.csv", index=False, encoding="utf-8")

group_selection = df.loc[df["Группа"] == "Гамма"].copy()
group_selection = group_selection.sort_values(
    by=["Среднее", "ID"],
    ascending=[False, True]
)
group_selection = group_selection[
    ["ID", "Имя", "Группа", "Среднее", "Посещаемость"]
]
print(group_selection)
group_selection.to_csv("group_selection.csv", index=False, encoding="utf-8")

group_summary = df.groupby("Группа").agg({
    "Среднее": ["mean", "min", "max", "count"],
    "Посещаемость": "mean",
    "Допуск": "sum"
})

group_summary = group_summary.reset_index()

group_summary.columns = [
    "Группа",
    "Средний_балл",
    "Минимальный_балл",
    "Максимальный_балл",
    "Количество_участников",
    "Средняя_посещаемость",
    "Количество_допущенных"
]
print(group_summary)

group_summary = group_summary.sort_values(
    by=["Средний_балл", "Группа"],
    ascending=[False, True]
)
print(group_summary)

group_summary.to_csv("results_summary.csv", index=False, encoding="utf-8")

source_before = pd.read_csv("source.csv")
print(source_before["Тест2"].count())
print(df["Тест2"].count())

admitted_ids = admitted["ID"].tolist()
attention_ids = attention["ID"].tolist()

common = []
for member_id in admitted_ids:
    if member_id in attention_ids:
        common.append(member_id)

all_ids = admitted_ids + attention_ids

print("Общие ID:", common)
print("Количество общих ID:", len(common))
print("Списки не пересекаются:", len(common) == 0)
print("Все участники учтены:", len(admitted_ids) + len(attention_ids) == 12)

gamma = df.loc[df["Группа"] == "Гамма"]

manual_mean = (
    gamma["Среднее"].iloc[0]
    + gamma["Среднее"].iloc[1]
    + gamma["Среднее"].iloc[2]
    + gamma["Среднее"].iloc[3]
) / 4

gamma_summary = df.groupby("Группа")["Среднее"].mean()
print(manual_mean)
print( gamma_summary.loc["Гамма"])