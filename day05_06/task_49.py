scores = [45, 82, 60, 39, 95, 71, 54, 88, 73, 91]

minimal = scores[0]
for score in scores:
    if score < minimal:
        minimal = score

print("Минимальный балл:", minimal)
