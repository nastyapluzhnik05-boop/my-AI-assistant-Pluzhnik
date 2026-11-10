scores = [20, 15, 76, 34, 42, 57, 89, 47, 38, 60]

with open("scores.txt ", "w", encoding="utf-8") as file:
    for score in scores:
        file.write(str(score) + "\n")