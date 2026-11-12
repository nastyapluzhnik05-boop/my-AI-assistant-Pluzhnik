from pathlib import Path
import csv
print(Path.cwd())

normalized_dir = Path("normalized")
chunks_dir = Path("chunks")
files = list(normalized_dir.glob("*.txt"))

chunk_size = 200
overlap = 40
minimum_length = 30
all_chunks = []
total_length = 0


def split_with_overlap(text, chunk_size, overlap, minimum_length):
    chunks = []
    step = chunk_size - overlap

    for start in range(0, len(text), step):
        if overlap <= chunk_size:
            chunk = text[start:start + chunk_size].strip()
            if chunk != "" and len(chunk) >= minimum_length:
                chunks.append(chunk)
        else:
            raise ValueError("overlap должен быть меньше chunk_size")
    return chunks

step = chunk_size - overlap

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = split_with_overlap(text, chunk_size, overlap, minimum_length)

    for chunk_id, chunk in enumerate(chunks):
        all_chunks.append({
            "source": file.name,
            "chunk_id": chunk_id,
            "text": chunk
        })
for chunk in all_chunks:
    total_length = total_length + len(chunk["text"])
    print("---")
    print(chunk["source"], chunk["chunk_id"])
    print("---")
    print(chunk["text"])
    print("Длина чанка:", len(chunk["text"]))
    source_stem = Path(chunk["source"]).stem
    filename = f"{source_stem}_chunk_{chunk['chunk_id']}.txt"
    output_path = chunks_dir / filename
    output_path.write_text(chunk["text"], encoding="utf-8")

if len(all_chunks) > 0:
    average = total_length / len(all_chunks)
    print("Средняя длина:", round(average, 1))
    print("Всего чанков:", len(all_chunks))
    print("Всего файлов:", len(files))

with open("chunks_summary.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["source", "chunk_id", "length"])
    for chunk in all_chunks:
        writer.writerow([
            chunk["source"],
            chunk["chunk_id"],
            len(chunk["text"])
        ])