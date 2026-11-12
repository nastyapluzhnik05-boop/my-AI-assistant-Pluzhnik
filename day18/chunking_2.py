from pathlib import Path

source_dir = Path("normalized")
files = list(source_dir.glob("*.txt"))
file_path = max(files, key=lambda file: file.stat().st_size)
text = file_path.read_text(encoding="utf-8")

print("Выбранный файл:", file_path.name)
print("Размер текста:", len(text))

def split_with_overlap(text, chunk_size, overlap, minimum_length):
    if overlap >= chunk_size:
        raise ValueError("overlap должен быть меньше chunk_size")

    chunks = []
    step = chunk_size - overlap

    for start in range(0, len(text), step):
        chunk = text[start:start + chunk_size].strip()

        if chunk != "" and len(chunk) >= minimum_length:
            chunks.append(chunk)

    return chunks

chunks_100 = split_with_overlap(text, 100, 10, 30)
chunks_200 = split_with_overlap(text, 200, 10, 30)

for folder_name, chunks in [
    ("chunks_100", chunks_100),
    ("chunks_200", chunks_200)
]:
    output_dir = Path(folder_name)
    output_dir.mkdir(exist_ok=True)

    for chunk_id, chunk in enumerate(chunks):
        output_path = output_dir / f"chunk_{chunk_id}.txt"
        output_path.write_text(chunk, encoding="utf-8")

print("Размер чанка 100:", len(chunks_100))
print("Размер чанка 200:", len(chunks_200))

print("Разница:", abs(len(chunks_100) - len(chunks_200)))