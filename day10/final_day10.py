
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")
print(df.head())
print(df.info())

summary = df.groupby("Группа").agg(
    mean=("Баллы", "mean"),
    min=("Баллы", "min"),
    max=("Баллы", "max"),
    count=("Баллы", "count"),
    Посещаемость=("Посещаемость", "mean")
)

summary = summary.reset_index()
summary = summary.sort_values("mean", ascending=False)
print(summary)

summary.to_csv("group_summary.csv", index=False, encoding="utf-8")

plt.bar(summary["Группа"], summary["mean"])
plt.title("Средний балл по группам")
plt.xlabel("Группа")
plt.ylabel("Средний балл")
plt.grid(axis="y")
plt.savefig("group_summary.png")
plt.show()
