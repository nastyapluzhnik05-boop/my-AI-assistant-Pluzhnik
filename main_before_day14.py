
print("Помощник в выборе подарка")
import os
from dotenv import load_dotenv # Загрузка настроек из файла .env
from gigachat import GigaChat
from prompts import SYSTEM_PROMPT
from gigachat.models import ChatCompletionRequest, ChatMessage, ChatModelOptions

load_dotenv()
key = os.getenv("GIGACHAT_CREDENTIALS")
scope = os.getenv("GIGACHAT_SCOPE")

recipient = input("Кому выбираем подарок и что человек любит? ").strip()
budget = input("Какой бюджет и чего нужно избегать? ").strip()
result_format = input("Что нужно получить: несколько идей или один лучший вариант? ").strip()
occasion = input("Какой повод для подарка? (необязательно): ").strip()
mode = input(
    "Выберите формат ответа: 1 — краткий, 2 — подробный: "
).strip()

if not occasion:
    occasion = "не указано"

if not recipient or not budget or not result_format:
    print("Введите все обязательные поля ещё раз, пожалуйста. Они не должны быть пустыми.") # проверка работоспособности кода при отправке пустой строки
elif mode not in ("1", "2"):
    print("Ошибка: введите 1 или 2.")
else:
    if mode == "1":
        response_style = "Отвечай кратко, без лишних объяснений."
    else:
        response_style = "Отвечай подробно, объясняя преимущества и причины рекомендации."
    
    user_prompt = f"""
    Кому выбираем подарок: {recipient}
    Бюджет и ограничения: {budget}
    Желаемый результат: {result_format}
    Повод: {occasion}
    Формат ответа: {response_style}
    """
    print("Сформированный запрос:")
    print(user_prompt)

    request = ChatCompletionRequest(  # Собираем запрос из системной инструкции и сообщения пользователя
        model_options=ChatModelOptions(
            temperature=0.2,
            max_tokens=400,
            repetition_penalty=1.0
        ),
        messages=[
            ChatMessage(
                role="system",
                content=SYSTEM_PROMPT,   # Использование промта из файла, передаём системную инструкцию
            ),
            ChatMessage(
                role="user",
                content=user_prompt,
            )
        ]
    )

    print("Отправляем запрос....")
    with GigaChat(   # передача данных гигачаду с определёнными настройками
        credentials=key,
        scope=scope,
        model="GigaChat-2",
        ca_bundle_file="certs/russian_trusted_root_ca_pem.crt",   # Указываем сертификат для защищённого соединения
        timeout=60,
    ) as client:   # Отправляем запрос модели и получаем ответ
        response = client.chat.create(request)
        answer = response.messages[0].content[0].text  # Извлекаем текст ответа из полученного результата
        print("Ответ:")
        print(answer)
        with open("last_prompt.txt", "w", encoding="utf-8") as file:
            file.write(user_prompt)
        with open("last_answer.txt", "w", encoding="utf-8") as file:
            file.write(answer)
        print("Запрос и ответ сохранены в файлы.")

