import numpy as np

scores = []
with open("scores_extra.txt", "r", encoding="utf-8") as file:
    for line in file:
        scores.append(int(line.strip()))

a = np.array(scores)
print("Среднее:", np.mean(a))
