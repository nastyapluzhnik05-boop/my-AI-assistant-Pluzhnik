from pathlib import Path

python_dir = Path("Python_basics")
files = list(python_dir.glob("*.txt"))

documents = []

for file_path in files:
    print(file_path.name)
    text = file_path.read_text(encoding="utf-8")
    document = {
        "source": file_path.name,
        "text": text
    }
    documents.append(document)

lines = text.splitlines()
clean_line =[]

def clean_text(text):
    lines = text.splitlines()
    clean_lines = []

    for line in lines:
        line = line.strip()
        if line != "":
            clean_lines.append(line)

    return "\n".join(clean_lines)

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
min_chars = 1000
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



    