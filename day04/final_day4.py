title = input("Введите название проекта: ")
author = input("Введите имя автора: ")
group = input("Введите имя группы: ")
members = int(input("Введите количество участников: "))
status = input("Введите статус проекта: ")

technologies = ["ИИ", "программирование", "графический дизайн"]

project = {
    "title": title,
    "author": author,
    "group": group,
    "members": members,
    "status": status,
    "technologies": technologies
}

print("=" * 30)
print(" " * 6 + project["title"])
print("=" * 30)

print(project["author"])
print(project["members"])
print(project["technologies"])
print(project["technologies"][0])
print(project["technologies"][-1])
print(len(project["technologies"]))

new_technology = input("Введите новую технологию: ")
if new_technology in project["technologies"]:
    print("Эта технология уже есть")
else:
    project["technologies"].append(new_technology)
    print("Технология добавлена")

technology_name = input("Введите название технологии: ")
 
if technology_name in project["technologies"]:
    print("Есть в списке")
else:
    print("Нет в списке")

new_status = input("Введите обновленный статус: ")
project["status"] = new_status

print(project)