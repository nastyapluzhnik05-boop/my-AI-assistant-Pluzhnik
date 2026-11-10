import numpy as np

M = np.array([
    [56, 64, 72],
    [78, 82, 86],
    [90, 94, 88],
    [62, 0, 70],
    [72, 76, 80],
    [42, 57, 52],
    [82, 86, 90],
    [60, 66, 62],
    [92, 96, 94],
    [68, 72, 74],
    [74, 0, 78],
    [50, 54, 58]
])

print(M)
print(type(M))
print(M.dtype)
print(M.ndim)
print(M.shape)
print(M.size)

print("Первая строка:", M[0])
print("Последняя строка:", M[-1])
print("Второй столбец", M[:, 1])
print(M[:4, :2])

print("Сумма баллов каждого студента:")
print(np.sum(M, axis=1))

print("Средний балл каждого студента:")
print(np.mean(M, axis=1).round(1))

print("Средний балл по каждому тесту:")
print(np.mean(M, axis=0).round(1))

print("Сумма всех баллов:", np.sum(M))
print("Среднее всех баллов:", np.mean(M))

print("Минимальный балл:", np.min(M))
print("Максимальный балл:", np.max(M))

T = 67
P = 76

attendance = np.array([
    71, 83, 91, 77, 80, 69,
    93, 75, 96, 81, 78, 73
])

averages = np.mean(M, axis=1)
ids = np.arange(1, 13)

mask = (averages >= T) & (attendance >= P)

print("ID студентов со средним баллом >= T и посещаемостью >= P:")
print(ids[mask])

numbers = np.arange(1, 37)

table = numbers.reshape(12, 3)
print(table)

zeros = np.zeros((12, 3))
print(zeros)
ones = np.ones((12, 3))
print(ones)
print(zeros + ones)

total_sum = np.sum(M)
total_mean = np.mean(M)

with open("results_numpy_report.txt", "w", encoding="utf-8") as file:
    file.write(f"Общая сумма баллов: {total_sum}\n")
    file.write(f"Среднее всех баллов: {total_mean}\n")

M_copy = M.copy()

M_copy[0, 2] = M_copy[0, 2] + 6

print("Исходный массив:")
print(M)

print("Изменённая копия:")
print(M_copy)

print("Исходная сумма:", np.sum(M))
print("Новая сумма:", np.sum(M_copy))

print("Исходное среднее:", np.mean(M))
print("Новое среднее:", np.mean(M_copy))

print("Средние по студентам до изменения:")
print(np.mean(M, axis=1).round(2))

print("Средние по студентам после изменения:")
print(np.mean(M_copy, axis=1).round(2))