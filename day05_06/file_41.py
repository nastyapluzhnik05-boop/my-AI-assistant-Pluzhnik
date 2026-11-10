import numpy as np
scores = [67, 90, 45, 34, 27, 68, 85, 84, 93]
passed = 0
for score in scores:
    if score >= 60:
        passed += 1
print(passed)
result = passed / len(scores) * 100

report = "Процент зачетов: " + str(round(result, 1)) + "%"
with open("report.txt", "a", encoding="utf-8") as file:
    file.write(report + "/n")
print(report)