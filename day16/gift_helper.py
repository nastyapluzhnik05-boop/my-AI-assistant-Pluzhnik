from pathlib import Path

gift_dir = Path("gift")

files = list(gift_dir.glob("*.txt"))

documents = []

for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    document = {
        "source": file_path.name,
        "text": text
    }
    documents.append(document)
    print(file_path.name, "-", len(document["text"]))
print(len(documents))
