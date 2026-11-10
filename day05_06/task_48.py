scores = [45, 82, 60, 39, 95, 71, 54, 88, 73, 91]

best = scores[0]
for score in scores:
    if score > best:
        best = score

print("Максимальный балл:", best)

