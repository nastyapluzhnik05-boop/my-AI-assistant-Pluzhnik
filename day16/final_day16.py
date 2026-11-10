from pathlib import Path

def clean_text(text):
    lines = text.splitlines()
    clean_lines = []
    for line in lines:
        clean_line = line.strip()

        if clean_line != "":
            clean_lines.append(clean_line)
        
    return "\n".join(clean_lines)

gift_dir = Path("gift")
files = list(gift_dir.glob("*.txt"))

documents =[]
documents_cleaned =[]

for file_path in files:
    print(file_path.name)
    text = file_path.read_text(encoding="utf-8")
    
    document = {
        "source": file_path.name,
        "text": text
    }
    if text.strip() != "":
        documents.append(document)
    
    text = clean_text(text)
    if text != "":
        documents_cleaned.append({
            "source": file_path.name,
            "text": text
        })
    else:
        print("Внимание, пустой документ:", document["source"])

cleaned_dir = Path("cleaned")
cleaned_dir.mkdir(exist_ok=True)

total_chars = 0

for document in documents_cleaned:
    output_path = cleaned_dir / document["source"]
    output_path.write_text(document["text"], encoding="utf-8")
    chars = len(document["text"])
    print(document["source"], "-", "символов", chars)
    total_chars = total_chars + chars
    if len(document["text"]) < 50:
        print(f"Документ {document['source']} слишком короткий (меньше 50 символов)")
print("Всего символов:", total_chars)
print("Документов:", len(documents_cleaned))




