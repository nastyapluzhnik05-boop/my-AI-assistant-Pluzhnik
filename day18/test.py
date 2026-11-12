text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chunk_size = 10

chunks = []

for start in range(0, len(text), chunk_size):
    chunk = text[start:start + chunk_size]
    chunks.append(chunk)

def split_into_chunks(text, chunk_size):
    chunks = []
    for start in range(0, len(text), chunk_size):
        chunk = text[start:start + chunk_size]
        chunks.append(chunk)
    return chunks

text = "Очень длинный учебный текст..."
chunks = split_into_chunks(text, 100)

for chunk in chunks:
    print(chunk)
    print("---")

def split_with_overlap(text, chunk_size, overlap):
    chunks = []
    step = chunk_size - overlap

    for start in range(0, len(text), step):
        chunk = text[start:start + chunk_size]
        chunks.append(chunk)

    return chunks

def split_with_overlap(text, chunk_size, overlap):
    if chunk_size <= 0:
        raise ValueError("chunk_size должен быть больше 0")
    if overlap < 0:
        raise ValueError("overlap не может быть отрицательным")
    if overlap >= chunk_size:
        raise ValueError("overlap должен быть меньше chunk_size")

    chunks = []
    step = chunk_size - overlap

    for start in range(0, len(text), step):
        chunk = text[start:start + chunk_size]
        chunks.append(chunk)

    return chunks

chunk = text[start:start + chunk_size].strip()

if chunk != "":
    chunks.append(chunk)

minimum_length = 30

if len(chunk) >= minimum_length:
    chunks.append(chunk)

chunk_data = {
    "source": "python.txt",
    "chunk_id": 0,
    "text": "Python — язык программирования..."
}

result = []

for chunk_id, chunk in enumerate(chunks):
    result.append({
        "source": file_path.name,
        "chunk_id": chunk_id,
        "text": chunk
    })

from pathlib import Path
import csv

def split_with_overlap(text, chunk_size, overlap, minimum_length=30):
    if chunk_size <= 0:
        raise ValueError("chunk_size должен быть больше 0")
    if overlap < 0:
        raise ValueError("overlap не может быть отрицательным")
    if overlap >= chunk_size:
        raise ValueError("overlap должен быть меньше chunk_size")

    chunks = []
    step = chunk_size - overlap

    for start in range(0, len(text), step):
        chunk = text[start:start + chunk_size].strip()
        if len(chunk) >= minimum_length:
            chunks.append(chunk)

    return chunks

source_dir = Path("normalized")
chunks_dir = Path("chunks")
chunks_dir.mkdir(exist_ok=True)

files = list(source_dir.glob("*.txt"))
all_chunks = []

for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    chunks = split_with_overlap(text, 300, 50)

    for chunk_id, chunk in enumerate(chunks):
        data = {
            "source": file_path.name,
            "chunk_id": chunk_id,
            "text": chunk
        }
        all_chunks.append(data)

        source_stem = file_path.stem
        filename = f"{source_stem}_chunk_{chunk_id}.txt"
        output_path = chunks_dir / filename
        output_path.write_text(chunk, encoding="utf-8")

with open("chunks_summary.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["source", "chunk_id", "length"])
    for chunk in all_chunks:
        writer.writerow([
            chunk["source"],
            chunk["chunk_id"],
            len(chunk["text"])
        ])

print("Документов:", len(files))
print("Всего чанков:", len(all_chunks))

with open("chunks_summary.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["source", "chunk_id", "length"])

    for chunk in all_chunks:
        writer.writerow([
            chunk["source"],
            chunk["chunk_id"],
            len(chunk["text"])
        ])

for start in range(0, len(text)):
    chunk = text[start:start + chunk_size]

for start in range(0, len(text), step):
    chunk = text[start:start + chunk_size]

filename = file_path.name + "_chunk_" + str(chunk_id) + ".txt"

text="ABCDEFGHIJ"
print(text[0:4])

chunk_size=10
overlap=3
step=chunk_size-overlap
print(step)

chunks=["A","B","C"]
for i,x in enumerate(chunks):
    print(i,x)
