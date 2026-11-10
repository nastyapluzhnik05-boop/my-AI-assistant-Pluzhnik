import numpy as np

scores = []
with open("scores_extra.txt", "r", encoding="utf-8") as file:
    for line in file:
        scores.append(int(line.strip()))

a = np.array(scores)
with open("numpy_report.txt", "w", encoding="utf-8") as file:
    file.write(f"Количество: {a.size}\n")
    file.write(f"Сумма: {np.sum(a)}\n")
    file.write(f"Среднее: {np.mean(a)}\n")
    file.write(f"Минимум: {np.min(a)}\n")
    file.write(f"Максимум: {np.max(a)}\n")
