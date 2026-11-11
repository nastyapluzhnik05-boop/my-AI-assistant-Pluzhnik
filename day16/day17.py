from pathlib import Path

def clean_line(text):
    line = text.replace("\t", " ")
    line = line.replace("\\t", " ")
    line = " ".join(line.split())
    return line

def normalize_text(text):
    lines = text.splitlines()
    clean_lines = []
    service_lines = [
        "черновик",
        "служебная копия"
    ]
    for line in lines:
        line = clean_line(line)
        normalized = line.lower()
        if normalized not in service_lines and line != "" and line not in clean_lines:
            clean_lines.append(line)
    return "\n".join(clean_lines)


corpus_dir = Path("corpus")
normalized_dir = Path("normalized")

normalized_dir.mkdir(exist_ok=True)
files = list(corpus_dir.glob("*.txt"))

total_before = 0
total_after = 0

for file_path in files:
    text = file_path.read_text(encoding="utf-8")

    normalized = normalize_text(text)
    output_path = normalized_dir / file_path.name
    output_path.write_text(normalized, encoding="utf-8")

    before = len(text)
    after = len(normalized)
    difference = before - after

    print(file_path.name)
    print(f"До: {before}, после: {after}")
    print(f"Удалено {difference} символов")

    total_before += len(text)
    total_after += len(normalized)

reduction = (total_before - total_after) / total_before * 100
print(f"Общий объём до: {total_before} символов")
print(f"Общий объём после: {total_after} символов")
print(f"Сокращение корпуса: {reduction:.2f}%")