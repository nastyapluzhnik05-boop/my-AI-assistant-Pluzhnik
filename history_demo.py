from gigachat.models import ChatMessage
from prompts import SYSTEM_PROMPT

messages = [
    ChatMessage(role="system", content=SYSTEM_PROMPT)
]

while True:
    user_text = input("Ты: ").strip()

    if user_text.lower() == "выход":
        print("Завершение программы.")
        break

    if not user_text:
        print("Сообщение не должно быть пустым.")
        continue

    messages.append(ChatMessage(role="user", content=user_text))

    answer = "Тестовый ответ без API"
    messages.append(ChatMessage(role="assistant", content=answer))

    if len(messages) > 7:
        messages = [messages[0]] + messages[-6:]
    
    print("Помощник:", answer)
    print("Количество сообщений:", len(messages))

    for message in messages:
        print(message.role)
