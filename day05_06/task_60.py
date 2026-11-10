technologies = ["Python", "NumPy", "Pandas", "Matplotlib", "Git", "SQL", "Jupyter"]

with open("technologies_numbered.txt", "w", encoding="utf-8") as file:
    for i in range(len(technologies)):
        file.write(f"{i + 1}. {technologies[i]}\n")
