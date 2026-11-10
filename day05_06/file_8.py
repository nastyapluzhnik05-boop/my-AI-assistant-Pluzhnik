technologies = ["AI", "программирование", "робототехника", "моделирование", "дизайн", "строительство"]
technology_name = input("Введите название технологии: ")

if technology_name in technologies:
    print(f"Технология '{technology_name}' есть в списке")
else:
    print("Технологии нет в списке")
