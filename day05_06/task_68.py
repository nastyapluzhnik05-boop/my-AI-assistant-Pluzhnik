scores = []
with open("scores_extra.txt", "r", encoding="utf-8") as file:
    for line in file:
        scores.append(int(line.strip()))

passed = 0
failed = 0
for score in scores:
    if score >= 60:
        passed += 1
    else:
        failed += 1

with open("summary.txt", "w", encoding="utf-8") as file:
    file.write(f"Количество баллов: {len(scores)}\n")
    file.write(f"Сумма: {sum(scores)}\n")
    file.write(f"Зачётов: {passed}\n")
    file.write(f"Незачётов: {failed}\n")
