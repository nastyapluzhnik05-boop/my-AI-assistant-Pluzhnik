with open("journal.txt", "w", encoding="utf-8") as file:
    file.write("Иванов" + "\n")
    file.write("Сидоров" + "\n")
    file.write("Петров" + "\n")

with open("journal.txt", "a", encoding="utf-8") as file:
    file.write("Козлова" + "\n")
    file.write("Мухин" + "\n")
