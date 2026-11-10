last_name = ["Мухина", "Медведев", "Козлова", "Бычков", "Глушкова", "Лебедева", "Синицина", "Петров", "Рыбкина", "Толкин"]
scores = [55, 84, 42, 72, 67, 98, 23, 89, 35, 47]

with open("group_report.txt ", "w", encoding="utf-8")as file:

    for i in range(len(last_name)):
        if scores[i] >= 60:
            status = "зачёт"
        else:
            status = "незачёт"

        line_to_write = f"{last_name[i]} - {scores[i]} - {status}\n"
        print(line_to_write)
        file.write(line_to_write)

passed = 0
failed = 0
for score in scores:
    if score >= 60:
        passed +=1
    else:
        failed +=1
print("Прошли:", passed)
print("Не прошли:", failed)

import numpy as np

a = np.array(scores)
print(a)
print(a.size, a.dtype, np.mean(a), np.sum(a), np.min(a), np.max(a))

below = a[a <= 60]
more = a[a>= 60]
print(below)
print(more)
print(a[:3])
print(a[7:])
a[1] = 78
print(a)

increased = a + 5
print(increased)
print(np.mean(increased))

with open("group_report.txt", "a", encoding="utf-8") as file:
    file.write(f"Прошли: {passed}\n")
    file.write(f"Не прошли: {failed}\n")
    file.write(f"Средний балл: {np.mean(a)}\n")
    file.write(f"Сумма баллов: {np.sum(a)}\n")
    file.write(f"Минимальный балл: {np.min(a)}\n")
    file.write(f"Максимальный балл: {np.max(a)}\n")

with open("group_report.txt ", "r", encoding="utf-8") as file:
    text = file.read()
print(text)

