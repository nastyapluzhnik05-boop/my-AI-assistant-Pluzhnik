surname = input("Фамилия нового студента: ")
score = int(input("Баллы: "))
with open("additions.txt", "w", encoding="utf-8") as file:
    file.write(surname + ":" + str(score) + "\n")