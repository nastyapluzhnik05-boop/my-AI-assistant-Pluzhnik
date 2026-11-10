import numpy as np

scores = []
with open("scores_extra.txt", "r", encoding="utf-8") as file:
    for line in file:
        scores.append(int(line.strip()))

a = np.array(scores)
average = np.mean(a)
above_average = a[a > average]
below_60 = a[a < 60]

print("Количество:", a.size)
print("Сумма:", np.sum(a))
print("Среднее:", average)
print("Минимум:", np.min(a))
print("Максимум:", np.max(a))
print("Выше среднего:", above_average)
print("Ниже 60:", below_60)

with open("final_extra_report.txt", "w", encoding="utf-8") as file:
    file.write(f"Количество: {a.size}\n")
    file.write(f"Сумма: {np.sum(a)}\n")
    file.write(f"Среднее: {average}\n")
    file.write(f"Минимум: {np.min(a)}\n")
    file.write(f"Максимум: {np.max(a)}\n")
    file.write(f"Выше среднего: {above_average}\n")
    file.write(f"Ниже 60: {below_60}\n")
