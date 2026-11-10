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
load_dotenv()

key = os.getenv("GIGACHAT_CREDENTIALS")
scope = os.getenv("GIGACHAT_SCOPE")

class AnalysisResult(BaseModel):
    topic: str
    category: str
    priority: int
    summary: str

logging.info("Начало работы программы")
prompt = input("Введите сообщение: ").strip()
count = 0

if not prompt:
        print("Сообщение не должно быть пустым")
        logging.warning("Введено пустое сообщение")
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
                response_format=AnalysisResult,
                strict=True
            )
            print(parsed.topic)
            print(parsed.category)
            print(parsed.priority)
            print(parsed.summary)
            logging.info("Успешное завершение программы")
            count += 1
            with open("result.txt", "w", encoding="utf-8") as file:
                file.write(parsed.topic + "\n")
                file.write(parsed.category + "\n")
                file.write(str(parsed.priority) + "\n")
                file.write(parsed.summary + "\n")
    except Exception as error:
        logging.error("Ошибка при обработке сообщения")
        print("Ошибка при обработке сообщения:", error)
