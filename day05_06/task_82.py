import numpy as np

scores = []
with open("scores_extra.txt", "r", encoding="utf-8") as file:
    for line in file:
        scores.append(int(line.strip()))

a = np.array(scores)
a[2] = 75

with open("corrected_scores.txt", "w", encoding="utf-8") as file:
    for score in a:
        file.write(f"{score}\n")

print(a)
