scores = [45, 82, 60, 39, 95, 71]

for i in range(len(scores)):
    if scores[i] >= 60:
        status = "зачёт"
    else:
        status = "незачёт"
    print(i + 1, scores[i], status)
