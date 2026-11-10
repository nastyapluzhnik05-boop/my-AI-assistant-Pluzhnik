with open("scores_extra.txt", "r", encoding="utf-8") as source:
    for line in source:
        score = int(line.strip())
        if score >= 60:
            with open("passed.txt", "w", encoding="utf-8") as passed:
                passed.write(str(score) + "\n")
        else:
            with open("failed.txt", "w", encoding="utf-8") as failed:
                failed.write(str(score) + "\n")
