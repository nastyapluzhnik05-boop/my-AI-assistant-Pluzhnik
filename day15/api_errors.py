import os
from dotenv import load_dotenv
from gigachat import GigaChat
import logging
from pydantic import BaseModel, Field

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logging.info("Начало работы программы")

class TopicAnalysis(BaseModel):
    category: str = Field(description="категория")
    priority: int = Field(description="приоритет")
    summary: str = Field(description="краткий вывод")

load_dotenv()

key = os.getenv("GIGACHAT_CREDENTIALS")
scope = os.getenv("GIGACHAT_SCOPE")
prompt = input("Введите сообщение: ").strip()

if prompt == "":
    print("Сообщение не должно быть пустым")
    logging.warning("Получен пустой ввод")
else:
    try:
        with GigaChat(
        credentials=key,
        scope=scope,
        model="GigaChat-2",
        ca_bundle_file="certs/russian_trusted_root_ca_pem.crt"
        ) as client:
            completion, parsed = client.chat_parse(
                prompt,
                response_format=TopicAnalysis,
                strict=True
            )
            print(parsed.category)
            print(parsed.priority)
            print(parsed.summary)
            logging.info("Успешное завершение программы")
    except Exception as error:
        print("Не удалось получить структурированный ответ")
        logging.error("Ошибка structured output: %s", error)




