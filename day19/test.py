from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

vector_a = [[1.0, 0.0, 0.0]]
vector_b = [[0.9, 0.1, 0.0]]

score = cosine_similarity(vector_a, vector_b)
print(score[0][0])

text = "Python — язык программирования"
embedding = model.encode(text)

print(type(embedding))
print(len(embedding))
print(embedding[:10])

texts = [
    "Как создать список в Python?",
    "Как работают списки Python?",
    "Какая сегодня погода?"
]

embeddings = model.encode(texts)
print(embeddings.shape)

similarities = model.similarity(embeddings, embeddings)
print(similarities)

texts = [
    "Как создать список в Python?",
    "Как работают списки Python?"
]

embeddings = model.encode(texts)
similarities = model.similarity(embeddings, embeddings)

print(similarities[0][1])

chunks = [
    "Списки Python создаются с помощью квадратных скобок.",
    "Git commit сохраняет изменения в истории.",
    "DataFrame — основная таблица Pandas."
]

chunk_embeddings = model.encode(chunks)
query = "Как создать список?"
query_embedding = model.encode(query)

scores = model.similarity(query_embedding, chunk_embeddings)
print(scores)

scores_list = scores[0].tolist()
print(scores_list)

best_score = max(scores_list)
best_index = scores_list.index(best_score)

print("Лучший индекс:", best_index)
print("Лучший чанк:", chunks[best_index])
print("Сходство:", best_score)

chunks = [
    {
        "source": "python.txt",
        "chunk_id": 0,
        "text": "Списки Python создаются с помощью квадратных скобок."
    },
    {
        "source": "git.txt",
        "chunk_id": 0,
        "text": "Git commit сохраняет изменения в истории."
    }
]

texts = [chunk["text"] for chunk in chunks]
chunk_embeddings = model.encode(texts)

texts = []

for chunk in chunks:
    texts.append(chunk["text"])

for i in range(len(chunks)):
    chunks[i]["embedding"] = chunk_embeddings[i].tolist()

print(chunks[0].keys())

query = input("Введите вопрос: ")
query_embedding = model.encode(query)

texts = [chunk["text"] for chunk in chunks]
chunk_embeddings = model.encode(texts)
scores = model.similarity(query_embedding, chunk_embeddings)[0].tolist()

best_score = max(scores)
best_index = scores.index(best_score)
best_chunk = chunks[best_index]

print("Источник:", best_chunk["source"])
print("Чанк:", best_chunk["chunk_id"])
print("Текст:", best_chunk["text"])
print("Сходство:", best_score)

top_k = 3

results = []

for i in range(len(chunks)):
    results.append({
        "index": i,
        "score": scores[i]
    })

results = sorted(results, key=lambda item: item["score"], reverse=True)

for result in results[:3]:
    chunk = chunks[result["index"]]
    print(result["score"], chunk["source"], chunk["text"])

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

chunks = [
    {"source": "python.txt", "chunk_id": 0, "text": "Списки Python создаются через квадратные скобки."},
    {"source": "git.txt", "chunk_id": 0, "text": "git commit сохраняет изменения в истории."},
    {"source": "pandas.txt", "chunk_id": 0, "text": "DataFrame используется для табличных данных."}
]

texts = []
for chunk in chunks:
    texts.append(chunk["text"])

chunk_embeddings = model.encode(texts)

query = input("Введите вопрос: ")
query_embedding = model.encode(query)

scores = model.similarity(query_embedding, chunk_embeddings)[0].tolist()
best_score = max(scores)
best_index = scores.index(best_score)
best_chunk = chunks[best_index]

print("Источник:", best_chunk["source"])
print("Текст:", best_chunk["text"])
print("Сходство:", round(best_score, 4))
