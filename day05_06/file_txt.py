name = input("Введите имя: ")
last_name = input("Введите фамилию: ")
group = input("Введите группу: ")
speciality = input("Ваша специальность: ")

with open("student.txt", "w", encoding="utf-8") as file:
    file.write("Имя:" + name + "\n")
    file.write("Фамилия:" + last_name + "\n")
    file.write("Группа:" + group + "\n")
    file.write("Специальность:" + speciality + "\n")