with open("technologies_numbered.txt", "r", encoding="utf-8") as source:
    content = source.read()

with open("copy.txt", "w", encoding="utf-8") as destination:
    destination.write(content)
