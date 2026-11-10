count = 0
with open("journal.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line.strip():
            count += 1

print("Непустых строк:", count)
