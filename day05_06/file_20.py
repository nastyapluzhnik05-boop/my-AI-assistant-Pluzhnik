higher = 0
below = 0
with open("scores.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(int(line))
        if int(line) >= 60:
            higher += 1
        else:
            below += 1
    print("Больше 60:", higher)
    print("Ниже 60:", below)
        