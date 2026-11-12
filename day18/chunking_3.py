from pathlib import Path
import csv

normalized_dir = Path("normalized")
chunks_dir = Path("chunks_all")
chunks_dir.mkdir(exist_ok=True)

files = list(normalized_dir.glob("*.txt"))

chunk_size = 100
overlap = 10
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


for file_path in files:
    text = file_path.read_text(encoding="utf-8")

    chunks = split_with_overlap(
        text, chunk_size, overlap, minimum_length
    )

    for chunk_id, chunk in enumerate(chunks):
        all_chunks.append({
            "source": file_path.name,
            "chunk_id": chunk_id,
            "text": chunk
        })

        filename = f"{file_path.stem}_chunk_{chunk_id}.txt"
        output_path = chunks_dir / filename
        output_path.write_text(chunk, encoding="utf-8")

        total_length += len(chunk)

with open("chunks_summary2.csv", "w", encoding="utf-8-sig", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["source", "chunk_id", "length"])

    for chunk in all_chunks:
        writer.writerow([
            chunk["source"],
            chunk["chunk_id"],
            len(chunk["text"])
        ])

print("Всего исходных файлов:", len(files))
print("Всего чанков:", len(all_chunks))
print("Общая длина чанков:", total_length)

if all_chunks:
    average = total_length / len(all_chunks)
    print("Средняя длина чанка:", round(average, 1))