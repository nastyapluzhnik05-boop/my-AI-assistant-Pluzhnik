project_name = input("Введите название проекта: ")
name = input("Введите ваше имя: ")
members = input("Введите количество участников: ")
status = input("Какой у вас статус проекта? ")

project = {
    "project_name": project_name,
    "name": name,
    "members": members,
    "status": status
}
project["technologies"] = ["IT", "AI", "robotics"]

print(project["project_name"])
print(project["technologies"])
print(project["technologies"][0])
