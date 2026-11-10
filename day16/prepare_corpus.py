from pathlib import Path



corpus_dir = Path("corpus")

files = list(corpus_dir.glob("*.txt"))
print(files)
print(len(files))

for file_path in files:
    print(file_path.name)

text = Path("corpus/python.txt").read_text(encoding="utf-8")
print(text)

documents = []

for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    document = {
        "source": file_path.name,
        "text": text
    }
    documents.append(document)
print(documents)
print(len(documents))

for document in documents:
    if document["text"].strip() == "":
        print("Пустой документ:", document["source"])

for document in documents:
    print(document["source"], len(document["text"]))
    if len(document["text"]) < 50:
        print("Внимание: короткий документ ", document["source"])

lines = text.splitlines()
clean_lines = []

for line in lines:
    clean_line = line.strip()
    if clean_line != "":
        clean_lines.append(clean_line)

clean_text = "\n".join(clean_lines)

def clean_text(text):
    lines = text.splitlines()
    clean_lines = []

    for line in lines:
        line = line.strip()
        if line != "":
            clean_lines.append(line)

    return "\n".join(clean_lines)

documents = []

for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    text = clean_text(text)

    if text != "":
        documents.append({
            "source": file_path.name,
            "text": text
        })
cleaned_dir = Path("cleaned")
cleaned_dir.mkdir(exist_ok=True)

total_chars = 0
total_document = []
max_chars = 0
min_chars = 700
for document in documents:
    chars = len(document["text"])
    total_chars = total_chars + chars
    print(document["source"], "—", chars, "символов")
    if chars > max_chars:
        max_chars = chars
        total_document = document["source"]
    if chars < min_chars and len(document["text"]) != "":
        min_chars = chars
        total_document2 = document["source"]
print("Всего символов:", total_chars)
print("Самый большой документ:", total_document, "количество символов:", max_chars)
print("Самый маленький документ:", total_document2, "количество символов:", min_chars)

