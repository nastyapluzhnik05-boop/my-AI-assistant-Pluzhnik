score = int(input("Введите балл от 0 до 100: "))
while score < 0 or score > 100:
    score = int(input("Ошибка. Введите балл от 0 до 100: "))

print("Принят балл:", score)
