try:
    with GigaChat(credentials=key) as client:
        response = client.chat.create("Привет")
except Exception as error:
    print("Ошибка:", error)
