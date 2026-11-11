from pathlib import Path

source_dir = Path("cleaned")
normalized_dir = Path("normalized")
normalized_dir.mkdir(exist_ok=True)

files = list(source_dir.glob("*.txt"))

for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    normalized = normalize_text(text)
    output_path = normalized_dir / file_path.name
    output_path.write_text(normalized, encoding="utf-8")

text = "Python\tGit\tPandas"
text = text.replace("\t", " ")
print(text)

text = "   Python   "
print(text.strip())

text = "Python    язык    программирования"
words = text.split()
clean_text = " ".join(words)
print(clean_text)

def clean_line(line):
    line = line.replace("\t", " ")
    line = " ".join(line.split())
    return line

lines = text.splitlines()
clean_lines = []

for line in lines:
    line = clean_line(line)
    if line != "":
        clean_lines.append(line)

result = "\n".join(clean_lines)

unique_lines = []

for line in clean_lines:
    if line not in unique_lines:
        unique_lines.append(line)

text = "Python PYTHON python"
print(text.lower())

def normalize_for_compare(text):
    text = " ".join(text.split())
    text = text.lower()
    return text

service_lines = [
    "черновик",
    "служебная копия"
]

normalized = line.lower()

if normalized not in service_lines:
    clean_lines.append(line)

text = text.replace("\u00a0", " ")
def clean_line(line):
    line = line.replace("\u00a0", " ")
    line = line.replace("\t", " ")
    line = " ".join(line.split())
    return line

def normalize_text(text):
    lines = text.splitlines()
    clean_lines = []

    for line in lines:
        line = clean_line(line)

        if line == "":
            continue

        if line not in clean_lines:
            clean_lines.append(line)

    return "\n".join(clean_lines)

before = len(text)
after = len(clean_text)

print("До:", before)
print("После:", after)
print("Удалено символов:", before - after)

if before > 0:
    percent = (before - after) / before * 100
    print("Сокращение:", round(percent, 1), "%")

for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    normalized = normalize_text(text)

    print("Файл:", file_path.name)
    print("До:", len(text))
    print("После:", len(normalized))
    print("---")
