print("Помощник в выборе подарка")
import os
from dotenv import load_dotenv # Загрузка настроек из файла .env
from gigachat import GigaChat
from prompts import SYSTEM_PROMPT
from gigachat.models import ChatCompletionRequest, ChatMessage, ChatModelOptions

load_dotenv()
key = os.getenv("GIGACHAT_CREDENTIALS")
scope = os.getenv("GIGACHAT_SCOPE")

messages = [
    ChatMessage(role="system", content=SYSTEM_PROMPT)
]

with open("chat_history.txt", "a", encoding="utf-8") as file:
    file.write("\n\n=== Новый запуск программы ===\n")

with GigaChat(
    credentials=key,
    scope=scope,
    model="GigaChat-2",
    ca_bundle_file="certs/russian_trusted_root_ca_pem.crt",
    timeout=60,
) as client:

    while True:
        user_text = input("Ты: ").strip()
        command = user_text.lower()

        if not user_text:
            print("Сообщение не должно быть пустым.")
            continue

        if command == "выход":
            print("Завершение программы.")
            break

        if command == "история":
            print("Количество сообщений:", len(messages))
            for message in messages:
                print(message.role)
            continue

        if command == "очистить":
            messages = [
                ChatMessage(role="system", content=SYSTEM_PROMPT)
            ]
            print("История диалога очищена.")
            with open("chat_history.txt", "a", encoding="utf-8") as file:
                file.write("=== История диалога очищена ===\n")
            continue

        messages.append(
            ChatMessage(role="user", content=user_text)
        )

        request = ChatCompletionRequest(
            model_options=ChatModelOptions(
                temperature=0.2,
                max_tokens=400,
                repetition_penalty=1.0
            ),
            messages=messages
        )

        print("Отправляем запрос...")
        response = client.chat.create(request)
        answer = response.messages[0].content[0].text

        print("Помощник:")
        print(answer)

        with open("chat_history.txt", "a", encoding="utf-8") as file:
            file.write(f"\nТы: {user_text}\n")
            file.write(f"Помощник: {answer}\n")

        messages.append(
            ChatMessage(role="assistant", content=answer)
        )

        if len(messages) > 7:
            messages = [messages[0]] + messages[-6:]

        print("Количество сообщений:", len(messages))