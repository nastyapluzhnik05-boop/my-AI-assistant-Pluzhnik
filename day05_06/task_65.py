scores = [45, 82, 60, 39, 95, 71, 54, 88, 73, 91]

with open("scores_extra.txt", "w", encoding="utf-8") as file:
    for score in scores:
        file.write(str(score) + "\n")
