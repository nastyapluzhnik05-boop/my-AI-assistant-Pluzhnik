import numpy as np
scores = []
with open("scores.txt", "r", encoding="utf-8") as file:
    for line in file:
        scores.append(int(line.strip()))
a = np.array(scores)

print("Сумма:", np.sum(a))
print("Среднее:", np.mean(a))
print("Минимум:", np.min(a))
print("Максимум:", np.max(a))
