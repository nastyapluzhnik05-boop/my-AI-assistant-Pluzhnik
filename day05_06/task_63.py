subjects = ["Python", "Математика", "История", "Основы Python", "Физика", "Программирование на Python", "Английский", "Базы данных"]

with open("subjects.txt", "w", encoding="utf-8") as file:
    for subject in subjects:
        file.write(subject + "\n")

with open("subjects.txt", "r", encoding="utf-8") as file:
    for line in file:
        if "Python" in line:
            print(line.strip())
