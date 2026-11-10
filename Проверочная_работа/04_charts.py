import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results_cleaned.csv")
group_summary = pd.read_csv("results_summary.csv")

plt.figure()

plt.bar(
    group_summary["Группа"],
    group_summary["Средний_балл"]
)

plt.title("Средний результат по группам. Вариант 17")
plt.xlabel("Группа")
plt.ylabel("Средний балл")
plt.grid(axis="y")

plt.tight_layout()
plt.savefig("results_group_average.png")
plt.show()
plt.close()

df = df.sort_values(by="ID")

plt.figure()

plt.plot(df["ID"], df["Среднее"], marker="o")

for i in range(len(df)):
    plt.text(
        df["ID"].iloc[i],
        df["Среднее"].iloc[i],
        str(df["ID"].iloc[i])
    )

plt.title("Средние результаты участников. Вариант 17")
plt.xlabel("ID участника")
plt.ylabel("Средний балл")
plt.xticks(df["ID"])

plt.tight_layout()
plt.savefig("results_participants.png")
plt.show()
plt.close()

plt.figure()

plt.bar(
    group_summary["Группа"],
    group_summary["Количество_допущенных"]
)

plt.title("Количество допущенных участников по группам. Вариант 17")
plt.xlabel("Группа")
plt.ylabel("Количество участников")
plt.yticks([0, 1, 2, 3, 4])
plt.grid(axis="y")

plt.tight_layout()
plt.savefig("results_admission.png")
plt.show()
plt.close()