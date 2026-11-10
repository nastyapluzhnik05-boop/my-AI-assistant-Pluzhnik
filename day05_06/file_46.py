numbers = [-8, 12, 0, 7, -3, 25, -1, 4, 0, 8]
positive = 0
negative = 0
zero = 0
for number in numbers:
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1

print("Положительные:", positive, "Отрицательные:", negative, "Нули:", zero)
