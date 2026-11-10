total = 0
with open("scores_extra.txt", "r", encoding="utf-8") as file:
    for line in file:
        total += int(line.strip())

print("Сумма баллов:", total)
