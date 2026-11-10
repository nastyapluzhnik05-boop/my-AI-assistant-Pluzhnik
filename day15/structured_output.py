result = Result(category="Python", difficulty="средняя", score=7)
print(result)
print(result.category)
print(result.score)

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)