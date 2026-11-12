from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path

model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

chunks_dir = Path("chunks")
files = list(chunks_dir.glob("*.txt"))

chunks = []
for file in files:
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()
    chunks.append({
        "source": file.name,
        "chunk_id": 0,
        "text": text
    })

texts = []
for chunk in chunks:
    texts.append(chunk["text"])

chunk_embeddings = model.encode(texts)
similarities = model.similarity(chunk_embeddings, chunk_embeddings)

for i in range(len(chunks)):
    chunks[i]["embedding"] = chunk_embeddings[i].tolist()

for i in range(3):
    query = input("Введите вопрос: ")
    query_embedding = model.encode(query)

    scores = model.similarity(query_embedding, chunk_embeddings)
    scores = scores[0].tolist()

    best_score = max(scores)
    best_index = scores.index(best_score)
    best_chunk = chunks[best_index]

    print("Источник:", best_chunk["source"])
    print("Номер чанка:", best_chunk["chunk_id"])
    print("Текст:", best_chunk["text"])
    print("Сходство:", round(best_score, 4))